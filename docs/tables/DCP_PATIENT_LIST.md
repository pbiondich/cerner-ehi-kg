# DCP_PATIENT_LIST

> Maintains the patient lists created by each user within PowerChart.

**Description:** DCP PATIENT LIST  
**Table type:** ACTIVITY  
**Primary key:** `PATIENT_LIST_ID`  
**Columns:** 10  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of the patient list. Should include the type of list as well as description of the filters applied to the list. |
| 2 | `NAME` | VARCHAR(50) | NOT NULL |  | Name of the patient list. Should be relatively short to maintain a nice display within applications. |
| 3 | `OWNER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the user that owns this list. |
| 4 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | PK | Unique identifier of patient list. |
| 5 | `PATIENT_LIST_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of patient list. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OWNER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BH_GROUP_DOC](BH_GROUP_DOC.md) | `PATIENT_LIST_ID` |
| [DCP_PL_ARGUMENT](DCP_PL_ARGUMENT.md) | `PATIENT_LIST_ID` |
| [DCP_PL_CUSTOM_ENTRY](DCP_PL_CUSTOM_ENTRY.md) | `PATIENT_LIST_ID` |
| [DCP_PL_ENCNTR_FILTER](DCP_PL_ENCNTR_FILTER.md) | `PATIENT_LIST_ID` |
| [DCP_PL_PRIORITIZATION](DCP_PL_PRIORITIZATION.md) | `PATIENT_LIST_ID` |
| [DCP_PL_RELTN](DCP_PL_RELTN.md) | `PATIENT_LIST_ID` |
| [DCP_PL_STATISTICS](DCP_PL_STATISTICS.md) | `PATIENT_LIST_ID` |

