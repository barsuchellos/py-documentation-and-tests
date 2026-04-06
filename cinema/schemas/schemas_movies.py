from drf_yasg import openapi

from cinema.serializers import MovieListSerializer

title_param = openapi.Parameter(
    "title",
    openapi.IN_QUERY,
    description="test title param, accepts only one title",
    type=openapi.TYPE_STRING,
)

genres_param = openapi.Parameter(
    "genres",
    openapi.IN_QUERY,
    description="accepts 'id' genre/s",
    type=openapi.TYPE_STRING,
)

actors_param = openapi.Parameter(
    "actors",
    openapi.IN_QUERY,
    description="test actors param, accepts 'id' actor/s",
    type=openapi.TYPE_STRING,
)

user_response = openapi.Response("response description", MovieListSerializer)
test_param = [title_param, genres_param, actors_param]
