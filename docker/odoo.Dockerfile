FROM odoo:18 AS builder

# Set environment variables
ENV HOST=db
ENV USER=odoo
ENV PASSWORD=odoo

# Switch to root user for installation
USER root

COPY ./docker/requirements.txt /usr/src/requirements.txt 
RUN pip install -r /usr/src/requirements.txt  --break-system-packages

FROM builder AS odoo

COPY ./odoo.conf /etc/odoo/odoo.conf
COPY ./addons /usr/addons

# Expose the Odoo default port
EXPOSE 8069

CMD ["odoo"]