# DCP_MP_PL_CUSTOM_ENTRY

> Stores the list of patients associated to a list for Dynamic Worklist

**Description:** DCP MPage Patient List Custom Entry  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_MP_PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | Identification of the custom patient list the entry is for. |
| 2 | `DCP_MP_PL_CUSTOM_ENTRY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DCP_MP_PL_CUSTOM_ENTRY table. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter this entry in the custom list pertains to. |
| 4 | `LAST_ACTION_DESC` | VARCHAR(100) |  |  | Describes the last qualifying action relevant to the custom entry. |
| 5 | `LAST_ACTION_DT_TM` | DATETIME |  |  | Identifies the date/time of the last qualifying action relevant to the custom entry. |
| 6 | `NEW_PATIENT_IND` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that this entry in the custom list pertains to. |
| 8 | `PERSON_PRIORITY_NBR` | DOUBLE |  |  | Allows the user to assign a priority to the person_ids within a patient list. |
| 9 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The group that owns the list of patients. So either the list of patients belongs to the patient_list_id or the prsnl_group_id. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_MP_PATIENT_LIST_ID` | [DCP_MP_PATIENT_LIST](DCP_MP_PATIENT_LIST.md) | `DCP_MP_PATIENT_LIST_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

