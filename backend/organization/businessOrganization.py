from models.organizations import Organizations
from models import db

class BusinessOrganization(object):
    @staticmethod
    def all_db_organizations():
        """Get all organizations from database"""
        orgs = Organizations.query.all()
        return orgs
    @staticmethod
    def create(received_organization):
        """Create a new organization"""
        if not received_organization:
            return

        new_organization = Organizations(organizationName=received_organization.Name, organizationURL=received_organization.URL)

        db.session.add(new_organization)
        db.session.commit()

        return new_organization.id

    @staticmethod
    def organization(organization_id):
        """Get a specific organization <organization_id>"""
        org = Organizations.query.filter(Organizations.id == organization_id).first()
        return org

    @staticmethod
    def update(organization_id, received_organization):
        """Update a specific organization"""
        if not received_organization:
            return False

        org = Organizations.query.filter(Organizations.id == organization_id).first()

        if org:
            org.organizationName = getattr( received_organization, 'Name', org.organizationName)
            org.organizationURL =  getattr( received_organization, 'URL', org.organizationURL)
            return True
        else:
            return False

    @staticmethod
    def delete(organization_id):
        """Delete a specific organization <organization_id>"""
        org = Organizations.query.filter(Organizations.id == organization_id).first()

        if org:
            db.session.delete(org)
            db.session.commit()
            return True
        else:
            return False