# INFOSCAN_PRODUCT

> InfoScan product Table

**Description:** InfoScan product  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORMULARY_IDENTIFIER` | VARCHAR(10) | NOT NULL |  | formulary identifierColumn |
| 2 | `MULTUM_FLAG` | DOUBLE |  |  | indicates which Multum tables to retrieve record from |
| 3 | `MULTUM_IDENTIFIER` | DOUBLE | NOT NULL |  | Multum identifierColumn |
| 4 | `MULTUM_NAME_CODE` | VARCHAR(11) | NOT NULL |  | Multum name codeColumn |
| 5 | `NOTE_IDENTIFIER` | VARCHAR(10) | NOT NULL | FK→ | note identifierColumn |
| 6 | `PROD_FORMU_STATUS_FLAG` | DOUBLE |  |  | product formulary status flagColumn |
| 7 | `THERAP_CLASS_IDENTIFIER` | DOUBLE | NOT NULL | FK→ | therapeutic class identifierColumn |
| 8 | `THERAP_SUB_CLASS_IDENTIFIER` | DOUBLE | NOT NULL | FK→ | therapeutic sub class identifierColumn |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_IDENTIFIER` | [INFOSCAN_NOTE](INFOSCAN_NOTE.md) | `NOTE_IDENTIFIER` |
| `THERAP_CLASS_IDENTIFIER` | [INFOSCAN_TC](INFOSCAN_TC.md) | `THERAP_CLASS_IDENTIFIER` |
| `THERAP_SUB_CLASS_IDENTIFIER` | [INFOSCAN_TC](INFOSCAN_TC.md) | `THERAP_SUB_CLASS_IDENTIFIER` |

