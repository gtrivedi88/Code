# Actions to perform after setting the user identity
    @flask_principal.identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Define the permission need for all users
        identity.provides.add(
            flask_principal.TypeNeed("all")
        )
        if not isinstance(identity, flask_principal.AnonymousIdentity):
            # Define the permission need for the user's roles
            for role in session['saml']['attributes']['Role']:
                identity.provides.add(
                    flask_principal.RoleNeed(role)
                )
            # Define the permission need for the user's groups
            for group in session['saml']['attributes']['group']:
                identity.provides.add(
                    flask_principal.Need('group', group)
                )
            # Define the permission need for an authenticated user
            identity.provides.add(
                flask_principal.TypeNeed("authenticated")
            )
        else:
            # Define the permission need for an anonymous user
            identity.provides.add(
                flask_principal.TypeNeed("anonymous")
            )
