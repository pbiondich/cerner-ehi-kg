# TRACKING_PREARRIVAL

> Tracking Pre-Arrival Information for EMS, doctor referral patients

**Description:** Tracking Pre-Arrival Information  
**Table type:** ACTIVITY  
**Primary key:** `TRACKING_PREARRIVAL_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_TXT` | VARCHAR(30) | NOT NULL |  | Free Text - age of patient |
| 3 | `ATTACHED_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Actual encntr_id of the pre-arrival patient. Will be back-filled after person/encounter data is available. |
| 4 | `ATTACHED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Actual person_id of the pre_arrival patient. Will be back-filled after encounter/person data is available. |
| 5 | `BIRTH_DT_TM` | DATETIME |  |  | Birth Date of Patient |
| 6 | `CHIEF_COMPLAINT` | VARCHAR(255) | NOT NULL |  | Presenting Problem of the patient |
| 7 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date time when pre-arrival record is created. |
| 8 | `ESTIMATED_ARRIVE_DT_TM` | DATETIME | NOT NULL |  | Patient Estimated Arrival Date and Time |
| 9 | `FIRST_NAME` | VARCHAR(200) | NOT NULL |  | Patient First Name - PERSON data not yet available |
| 10 | `LAST_NAME` | VARCHAR(200) | NOT NULL |  | Patient Last Name - PERSON data not yet available |
| 11 | `PCP_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Provider_id of the Primary care physician. FK from PRSNL |
| 12 | `PCP_PROVIDER_NAME` | VARCHAR(150) | NOT NULL |  | Free Text PCP Name. May be in liew of ID |
| 13 | `PREARRIVAL_TYPE_CD` | DOUBLE | NOT NULL |  | Prearrival type of patient |
| 14 | `REFERRING_SOURCE_ID` | DOUBLE | NOT NULL |  | PRSNL_ID of referring source provider |
| 15 | `REFERRING_SOURCE_NAME` | VARCHAR(150) | NOT NULL |  | Name of Referring Source (may be in liew of Personnel data) |
| 16 | `REG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person id who registers the Prearrival |
| 17 | `REG_PRSNL_NAME` | VARCHAR(150) | NOT NULL |  | Free Text Registration Prsnl Name (may be in liew of personnel data) |
| 18 | `SEX_CD` | DOUBLE | NOT NULL |  | Gender Code of the Patient |
| 19 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group Code |
| 20 | `TRACKING_PREARRIVAL_ID` | DOUBLE | NOT NULL | PK | Primary Key for the table Unique id for the table. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTACHED_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ATTACHED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PCP_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACKING_PREARRIVAL_USERFIELDS](TRACKING_PREARRIVAL_USERFIELDS.md) | `TRACKING_PREARRIVAL_ID` |

