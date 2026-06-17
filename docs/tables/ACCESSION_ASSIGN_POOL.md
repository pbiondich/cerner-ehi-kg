# ACCESSION_ASSIGN_POOL

> The templates for the accession buckets (accession_assignment table).

**Description:** Accession Assignment Pool  
**Table type:** REFERENCE  
**Primary key:** `ACCESSION_ASSIGNMENT_POOL_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ASSIGNMENT_POOL_ID` | DOUBLE | NOT NULL | PK | A system generated number that uniquely identifies an accession pool. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity type that is used to filter order catalog items within catalog type |
| 3 | `DESCRIPTION` | VARCHAR(50) |  |  | The description of the accession bucket. |
| 4 | `INCREMENT_VALUE` | DOUBLE |  |  | The increment value of an accession bucket. |
| 5 | `INITIAL_VALUE` | DOUBLE |  |  | The initial value of the accession bucket. |
| 6 | `RESET_FREQUENCY` | DOUBLE |  |  | Currently not used. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ACCESSION_ASSIGNMENT](ACCESSION_ASSIGNMENT.md) | `ACC_ASSIGN_POOL_ID` |
| [ACCESSION_ASSIGN_XREF](ACCESSION_ASSIGN_XREF.md) | `ACCESSION_ASSIGNMENT_POOL_ID` |
| [PREFIX_GROUP](PREFIX_GROUP.md) | `GROUP_ID` |

