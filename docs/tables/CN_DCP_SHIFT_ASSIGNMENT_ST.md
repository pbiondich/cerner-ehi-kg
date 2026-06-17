# CN_DCP_SHIFT_ASSIGNMENT_ST

> Houses shift assignment information for legal reporting and QI purposes.

**Description:** CN DCP SHIFT ASSIGNMENT ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNED_RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | The definition of the assignment that was made, (Charge Nurse, Secondary Nurse, On-Call Cardiologist, Sister, Brother). |
| 2 | `ASSIGNMENT_GROUP_CD` | DOUBLE | NOT NULL |  | The location group code for which this assignment was done, i.e. (Second Floor ICU, ED, etc.). |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CARETEAM_NAME` | VARCHAR(100) |  |  | The name of the care team the provider was a member of for the purpose of this assignment. |
| 5 | `CN_DCP_SHIFT_ASSIGNMENT_ST_ID` | DOUBLE | NOT NULL |  | Unique identifier for assignment |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | The bed location of the assignment. |
| 9 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | The building location of the assignment. |
| 10 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | The facility location of the assignment. |
| 11 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The room location of the assignment. |
| 12 | `LOC_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit location of the assignment. |
| 13 | `PCT_CARE_TEAM_ID` | DOUBLE | NOT NULL | FK→ | The Physician Care Team that this shift assignment pertains to. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the user assigned by this row. |
| 16 | `PRSNL_POS_CD` | DOUBLE | NOT NULL |  | The position of the assigned provider at the time of the assignment. |
| 17 | `RELATED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Supports relationships between a patient and a free-text person in Millennium, like Mother, Brother, Pastor, etc. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PCT_CARE_TEAM_ID` | [PCT_CARE_TEAM](PCT_CARE_TEAM.md) | `PCT_CARE_TEAM_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RELATED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

