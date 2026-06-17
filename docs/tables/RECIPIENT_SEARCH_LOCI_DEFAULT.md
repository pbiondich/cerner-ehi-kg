# RECIPIENT_SEARCH_LOCI_DEFAULT

> Specifies the default loci for which HLA typings should be displayed when potential recipients are listed in the Recipient Search application.

**Description:** Recipient Search Loci Default  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCI_CD` | DOUBLE | NOT NULL |  | The code for the specific HLA Loci to display for recipient phenotypes as the defaults in the Recipient Search application. |
| 2 | `LOCI_SEQ` | DOUBLE | NOT NULL |  | Arbitrarily assigned number to make each record unique and to determine the order the loci are displayed for recipient phenotypes as the defaults in the Recipient Search application. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

