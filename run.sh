gnome-terminal \
    --tab --title="Frontend" -- bash -ic "cd frontend && npm run dev; exec bash" 
gnome-terminal \
    --tab --title="Backend" -- bash -ic "cd backend && workon sw2 && python3 manage.py runserver; exec bash"