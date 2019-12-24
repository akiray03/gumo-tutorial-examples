import main


def test_tasks_view_success():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/tasks")
    assert r.status_code == 200
