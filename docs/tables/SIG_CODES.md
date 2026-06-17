# SIG_CODES

> Sig Codes - Stores SIG Codes for Prescriptions

**Description:** Sig Codes - Stores SIG code of Prescriptions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(200) |  |  | Translation for SIG Code (i.e. BID = twice a day) |
| 2 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Field Type |
| 3 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | Language |
| 4 | `SIG_CD` | DOUBLE | NOT NULL |  | sig |
| 5 | `SIG_TYPE_CD` | DOUBLE | NOT NULL |  | Sig Type |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALUE` | DOUBLE |  |  | Stores specific numeric values |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

