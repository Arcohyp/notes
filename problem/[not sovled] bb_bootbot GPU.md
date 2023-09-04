# Reporting errors of bb@nuc-bootbot

This issue is still opening, I have no idea of it, and I saw several people facing the same issue as me but no one reply. Now I just list the points that I have already known.

This is a simple code of what is ***amdgpu_get_auth(1)***, and I list the whole code at the end.
> https://lists.freedesktop.org/archives/dri-devel/2017-August/150839.html

Here is another ***error***:

** (gdmflexiserver:1759): WARNING **: Unable to create transient display: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.gnome.DisplayManager was not provided by any .service files.

When restart lightdm:

failed to open CK session: DBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.Consolekit was not provided by any .service files.

## Question: When using *rviz* or *rqt_tf_tree*, for example, terminal will show the errors as below:
    rviz
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2008-57-21.png)

Here are three main clues, or keywords:

> screen 0 does not appear to be DRI2 capable
>
> screen 0 does not appear to be DRI2 capable
> 
> amdgpu_device_initialize: amdgpu_get_auth (1) failed (-1)
>
> Segmentation fault

- GPU is ***[AMD/ATI] Polaris 22 [Radeon RX Vega M GL]***. 

- CPU is ***i7-8705G CPU @ 3.10GHz*** and architecture is ***x86_64***.

GPU is independent, but it binds to with CPU because CPU has a letter of ‘G’.

    lspci -vnn | grep VGA
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2008-59-09.png)

    lscpu
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2008-59-33.png)

    sudo lshw -C video
![image](https://github.com/Arcohyp/notes/blob/main/problem/pic/Screenshot%20from%202023-08-31%2009-14-11.png)

This is the whole code:

    On 22 January 2017 at 18:48, Emil Velikov <emil.l.velikov at gmail.com> wrote:
    > All one needs is to establish if dev->fd is the flink (primary/card)
    > node, rather than use DRM_IOCTL_GET_CLIENT to query the auth status.
    >
    > The latter is [somewhat] deprecated and incorrect. We need to know [and
    > store] the primary node FD, since we're going to use it [at a later
    > stage] for buffer import/export sharing.
    >
    > Cc: amd-gfx at lists.freedesktop.org
    > Signed-off-by: Emil Velikov <emil.l.velikov at gmail.com>
    > ---
    > Again not 100% sure but things look quite fishy as-is... The
    > conditionals might be off.
    >
    > Note: original code [and this one] do not consider if flink_fd is
    > already set, thus as we dup we'll leak it.
    > ---
    >  amdgpu/amdgpu_device.c | 43 ++-----------------------------------------
    >  1 file changed, 2 insertions(+), 41 deletions(-)
    >
    > diff --git a/amdgpu/amdgpu_device.c b/amdgpu/amdgpu_device.c
    > index f4ede031..6f04d936 100644
    > --- a/amdgpu/amdgpu_device.c
    > +++ b/amdgpu/amdgpu_device.c
    > @@ -101,34 +101,6 @@ static int fd_compare(void *key1, void *key2)
    >         return result;
    >  }
    >
    > -/**
    > -* Get the authenticated form fd,
    > -*
    > -* \param   fd   - \c [in]  File descriptor for AMD GPU device
    > -* \param   auth - \c [out] Pointer to output the fd is authenticated or not
    > -*                          A render node fd, output auth = 0
    > -*                          A legacy fd, get the authenticated for compatibility root
    > -*
    > -* \return   0 on success\n
    > -*          >0 - AMD specific error code\n
    > -*          <0 - Negative POSIX Error code
    > -*/
    > -static int amdgpu_get_auth(int fd, int *auth)
    > -{
    > -       int r = 0;
    > -       drm_client_t client = {};
    > -
    > -       if (drmGetNodeTypeFromFd(fd) == DRM_NODE_RENDER)
    > -               *auth = 0;
    > -       else {
    > -               client.idx = 0;
    > -               r = drmIoctl(fd, DRM_IOCTL_GET_CLIENT, &client);
    > -               if (!r)
    > -                       *auth = client.auth;
    > -       }
    > -       return r;
    > -}
    > -
    >  static void amdgpu_device_free_internal(amdgpu_device_handle dev)
    >  {
    >         amdgpu_vamgr_deinit(dev->vamgr);
    > @@ -175,8 +147,6 @@ int amdgpu_device_initialize(int fd,
    >         struct amdgpu_device *dev;
    >         drmVersionPtr version;
    >         int r;
    > -       int flag_auth = 0;
    > -       int flag_authexist=0;
    >         uint32_t accel_working = 0;
    >         uint64_t start, max;
    >
    > @@ -185,19 +155,10 @@ int amdgpu_device_initialize(int fd,
    >         pthread_mutex_lock(&fd_mutex);
    >         if (!fd_tab)
    >                 fd_tab = util_hash_table_create(fd_hash, fd_compare);
    > -       r = amdgpu_get_auth(fd, &flag_auth);
    > -       if (r) {
    > -               pthread_mutex_unlock(&fd_mutex);
    > -               return r;
    > -       }
    >         dev = util_hash_table_get(fd_tab, UINT_TO_PTR(fd));
    >         if (dev) {
    > -               r = amdgpu_get_auth(dev->fd, &flag_authexist);
    > -               if (r) {
    > -                       pthread_mutex_unlock(&fd_mutex);
    > -                       return r;
    > -               }
    > -               if ((flag_auth) && (!flag_authexist)) {
    > +               if (drmGetNodeTypeFromFd(fd) == DRM_NODE_RENDER &&
    > +                   drmGetNodeTypeFromFd(dev->fd) == DRM_NODE_PRIMARY) {
    >                         dev->flink_fd = dup(fd);
    >                 }
    >                 *major_version = dev->major_version;
    > --
    > 2.11.0
    >
