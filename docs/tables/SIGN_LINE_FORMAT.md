# SIGN_LINE_FORMAT

> This table includes the primary identification code and description for a signature line format. The signature line format attributes are stored on the SIGN_LINE_FORMAT_DETAIL table.

**Description:** Signature Line Format Table  
**Table type:** REFERENCE  
**Primary key:** `FORMAT_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(60) |  |  | This field contains the description established for the signature line format. |
| 3 | `FORMAT_ID` | DOUBLE | NOT NULL | PK | This internal identification code value uniquely identifies a row on this table. This value is used to join to other tables, such as the SIGN_LINE_FORMAT_DETAIL table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SIGN_LINE_DTA_R](SIGN_LINE_DTA_R.md) | `FORMAT_ID` |
| [SIGN_LINE_FORMAT_DETAIL](SIGN_LINE_FORMAT_DETAIL.md) | `FORMAT_ID` |
| [SIGN_LINE_LAYOUT_FIELD_R](SIGN_LINE_LAYOUT_FIELD_R.md) | `FORMAT_ID` |

