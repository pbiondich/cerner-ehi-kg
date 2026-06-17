# WORKLIST_ORDER_R

> Defines the relationship between a worklist and the orders included on a worklist.

**Description:** Worklist Order Resolution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | Defines the date and time the worklist order row was created. |
| 2 | `IDENTIFIER` | VARCHAR(20) |  |  | Identifies the accession by a number for the given worklist. (Currently not implemented) |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific order. Creates a relationship to the orders table. |
| 4 | `POST_TO_FLAG` | DOUBLE |  |  | Defines the current status of how the identifier has been used. (Currently not implemented) |
| 5 | `SEQUENCE` | DOUBLE |  |  | Defines the order in which the user has defined the accessions to display on a worklist. This sequence is stored on the worklist order resolution table and the accession order resolution table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific worklist. Creates a relationship to the worklist table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |

