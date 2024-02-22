# Web Infrastructure Design

## 0-simple_web_stack description:

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via ``www.foobar.com``. Start your explanation by having a user wanting to access your website.

You must use:

1_ physical server

2_ web server (Nginx)

3_ application server

4_ application files (your code base)

5_ database (MySQL)

* domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## 1-distributed_web_infrastructure description:

You must add to ``0-simple_web_stack``:

2 physical servers

1 web server (Nginx)

1 application server

1 load-balancer (HAproxy)

1 application files (your code base)

1 database (MySQL)

## 2-secured_and_monitored_web_infrastructure description:

You must add to ``distributed_web_infrastructure``:

3 firewalls

1 SSL certificate to serve www.foobar.com over HTTPS

3 monitoring clients (data collector for Sumologic or other monitoring services)

## 3-scale_up description:

You must add to 2-secured_and_monitored_web_infrastructure:

1 physical server

1 load-balancer (HAproxy) configured as cluster with the other one

* Split components (web server, application server, database) with their own server



