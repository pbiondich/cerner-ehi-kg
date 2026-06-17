# SIGN_LINE_LAYOUT_FIELD_R

> This table contains the relationships between the layout field used in Layout Builder with the signature line format.

**Description:** Signature Line Layout Field Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FORMAT_ID` | DOUBLE | NOT NULL | FK→ | This column contains the internal identification code representing the signature line format. This value is used to join to the signature line format information stored on the SIGN_LINE_FORMAT table. |
| 3 | `SIGN_LINE_LAYOUT_FIELD_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between a signature line and a layout field. |
| 4 | `STATUS_FLAG` | DOUBLE |  |  | This column contains a flag value representing the result status for which the signature line format is associated. Currently signature lines can be associated with : 1 - Performed2 - Verified and Corrected |
| 5 | `UCMR_LAYOUT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related stored layout field for Layout Builder. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORMAT_ID` | [SIGN_LINE_FORMAT](SIGN_LINE_FORMAT.md) | `FORMAT_ID` |
| `UCMR_LAYOUT_FIELD_ID` | [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `UCMR_LAYOUT_FIELD_ID` |

