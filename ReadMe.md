## Design considerations

As per my research I designed four models models which could be used to effectively record the interactions of a doctor and a Patient.
Those models are the following.

1. The User Model.
    - To record the user name and id(a formality)
2. The Doctor Model.
    - An extension to the user model.
3. The Patient Model.
   - An extension to the user model.
    
4. The Interaction Model.
   - This model is used to record all the interactions bwrtween doctor and patients.
   - The outcome field records the thoughts or the doctors during the patients first visit.
   - The diagnosis field records the diagnosis of the doctor.
   - The treatment is used to record the recommended treatment.

The application has endpoints which can acheive the following.
  - POST: **interactions/** to record create an interaction.
  - GET: **interactions/** to retrieve all interactions, it also has query params for filtering.
  - GET: **interactions/{id}** to get the interaction of the id.
  - GET: **report/{doctor_id}/{patient_id}/** to get the report using the doctor and patient id.

## Notes
  1. I decided to go against a dedicated model for history as I beleived it to be a over engineered solution.
  2. I also decided go against the text choices for Healty and Unhealthy as the outcomde can filtered using the query params.


## Testing the Application
Please follow the intructions below to run the application.

1. Git clone the repo.
2. CD into the cloned directory.
3. Run **docker-compose** build web contianer.
4. Run **docker-compose up**
5. Go to localhost:8004/docs to visit the swagger API.
6. Use the api's define there to test the app.
