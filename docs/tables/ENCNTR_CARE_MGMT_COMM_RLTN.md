# ENCNTR_CARE_MGMT_COMM_RLTN

> Links the communication recorded on the encntr_care_mgmt_comm table with one or more clinical results or discharge plans.

**Description:** Encounter Care Management Comunication Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_CARE_MGMT_COMM_ID` | DOUBLE | NOT NULL | FK→ | Reference to Encntr_Care_mgmt_comm table |
| 2 | `ENCNTR_CARE_MGMT_COMM_RLTN_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated number. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identify for the parent table for which the communication was sent for. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This is the table the parent_entity_id can be found on |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_CARE_MGMT_COMM_ID` | [ENCNTR_CARE_MGMT_COMM](ENCNTR_CARE_MGMT_COMM.md) | `ENCNTR_CARE_MGMT_COMM_ID` |

