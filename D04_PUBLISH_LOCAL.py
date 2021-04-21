import tableauserverclient as TSC

tableau_auth = TSC.TableauAuth('admin', 'xxxxxx', site_id='tug')
server = TSC.Server('http://tabserver')
server.auth.sign_in(tableau_auth)

proj_id = "xxxxxxxxxx"
hyper_file = "xxxxxxxxxxx/COVID.hyper"

new_ds = TSC.DatasourceItem(proj_id)
new_ds = server.datasources.publish(new_ds, hyper_file, "Overwrite")
print("Success")




