# DM_CORE_EOD_SI

> Store the disassembled versions of the End of Downtime Special Instructions text.

**Description:** DM_CORE_EOD_SI  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CORE_EOD_SI_ID` | DOUBLE | NOT NULL |  | Primary Key for the table |
| 2 | `INSTRUCTION_TXT` | VARCHAR(255) | NOT NULL |  | The text containing a single line of Special Instructions |
| 3 | `LINE_NUMBER` | DOUBLE | NOT NULL |  | Identifies the Line Number in the Special Instructions file for ordering |
| 4 | `OS_VERSION_NAME` | VARCHAR(10) | NOT NULL |  | Name of the OS Version for the files |
| 5 | `SI_RELEASE_IDENT` | DOUBLE | NOT NULL |  | Identifier for a set of Special Instructions. Internally generated number (not from a sequence) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VERSION_NUMBER` | DOUBLE | NOT NULL |  | Track versions of a given set of special instructions |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

