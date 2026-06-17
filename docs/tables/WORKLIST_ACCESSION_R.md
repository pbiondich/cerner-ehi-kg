# WORKLIST_ACCESSION_R

> Stores the Quality Control accessions included on a worklist.

**Description:** Worklist Accession Resolution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific QC accession included on a worklist. Creates a relationship to the accession table. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | Defines the date and time the QC accession row was created. |
| 3 | `IDENTIFIER` | VARCHAR(20) |  |  | Stores the user identifier entered in the worklist application and used by an instrument to post results when an accession is not sent by the instrument. (Currently not implemented) |
| 4 | `POST_TO_FLAG` | DOUBLE |  |  | Defines the current status of how the identifier has been used. (Currently not implemented) |
| 5 | `QC_GROUP_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific set of QC results that are included on a worklist. |
| 6 | `SEQUENCE` | DOUBLE | NOT NULL |  | Defines the numerical order that a QC accession should display on a worklist. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific worklist. Creates a relationship to the worklist table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |

