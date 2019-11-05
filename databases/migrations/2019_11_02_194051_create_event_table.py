from orator.migrations import Migration

class CreateEventTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Event') as table:
            table.increments('id')
            table.timestamps()
            table.string('name').unique()
            table.string('youtube_url').nullable()
            table.string('website_url').nullable()
            table.date('start_date').nullable()
            table.date('end_date').nullable()
            
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Event')
