from sightings.models import Comment, Sighting


class CommentService:

    @staticmethod
    def create_comment(sighting_id, text, user):
        sighting = Sighting.objects.get(id=sighting_id)
        return Comment.objects.create(
            user=user,
            sighting=sighting,
            text=text
        )

    @staticmethod
    def list_comments(sighting_id):
        return Comment.objects.filter(sighting_id=sighting_id)