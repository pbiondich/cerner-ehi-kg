# DCP_MP_PATIENT_LIST

> Stores the lists created for Dynamic Worklist

**Description:** DCP MP PATIENT LIST  
**Table type:** ACTIVITY  
**Primary key:** `DCP_MP_PATIENT_LIST_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_MP_PATIENT_LIST_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the table |
| 2 | `DEFAULT_LIST_IND` | DOUBLE | NOT NULL |  | Indicator for using Default List |
| 3 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | description of the patient list. should include the type of list as well as description of the filters applied to the list. |
| 4 | `NAME` | VARCHAR(50) | NOT NULL |  | name of the patient list. should be relatively short to maintain a nice display within applications. |
| 5 | `OWNER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the id of the user that owns this list. |
| 6 | `PATIENT_LIST_TYPE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OWNER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DCP_MP_PL_CUSTOM_ENTRY](DCP_MP_PL_CUSTOM_ENTRY.md) | `DCP_MP_PATIENT_LIST_ID` |
| [DCP_PL_ARGUMENT](DCP_PL_ARGUMENT.md) | `DCP_MP_PATIENT_LIST_ID` |
| [DCP_PL_RELTN](DCP_PL_RELTN.md) | `DCP_MP_PATIENT_LIST_ID` |

