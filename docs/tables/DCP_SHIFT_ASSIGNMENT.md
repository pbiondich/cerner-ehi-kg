# DCP_SHIFT_ASSIGNMENT

> Shift locaition asssignments for users.

**Description:** DCP SHIFT ASSIGNMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSIGNED_RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | The definition of the assignment that was made, (Charge Nurse, Secondary Nurse, On-Call Cardiologist, Sister, Brother). |
| 3 | `ASSIGNMENT_GROUP_CD` | DOUBLE | NOT NULL |  | The location group code for which this assignment was done, i.e. (Second Floor ICU, ED, etc.). |
| 4 | `ASSIGNMENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for assignment |
| 5 | `ASSIGNMENT_POS_CD` | DOUBLE | NOT NULL |  | The position_cd of the user making the assignment. In conjunction with the assignment_group_cd it identifies a a set of assignments made for a particular department.(RN, LPN, etc.). |
| 6 | `ASSIGN_TYPE_CD` | DOUBLE | NOT NULL |  | Clinical venue or discipline for the assignment, (Nursing, Cardiology, Respiratory Therapy, etc.) |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CARETEAM_ID` | DOUBLE | NOT NULL |  | The id of the care team that the assignment is for. If this field is set then prsnl_id should be 0. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | Bed |
| 12 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | Building |
| 13 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Facility |
| 14 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | Room |
| 15 | `LOC_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Unit |
| 16 | `PCT_CARE_TEAM_ID` | DOUBLE | NOT NULL | FK→ | The Physician Care Team that this shift assignment pertains to. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 18 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the prsnl that the assignment is for. If this field is filled out the care team_id should be 0. |
| 19 | `PURGE_IND` | DOUBLE |  |  | The row is marked ready to purge once it has been migrated to the CN_DCP_SHIFT_ASSIGNMENT_ST table. |
| 20 | `RELATED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Supports relationships between a patient and a free-text person in Millennium, like Mother, Brother, Pastor, etc. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PCT_CARE_TEAM_ID` | [PCT_CARE_TEAM](PCT_CARE_TEAM.md) | `PCT_CARE_TEAM_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RELATED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

