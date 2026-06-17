# SIGN_LINE_EP_R

> This table contains the relationships between the encounter pathway used in Case Integration with the signature line format.

**Description:** Sign Line Encounter Pathway Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CKI_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | This column indicates the CKI Identifier of the pattern selected to be associated with the given signature line. This identifier originates in the SCR Pattern table. |
| 3 | `CKI_SOURCE` | VARCHAR(12) | NOT NULL |  | This column indicates the CKI Source of the pattern selected to be associated with the given signature line. this identifier originates in the SCR Pattern Table. |
| 4 | `FORMAT_ID` | DOUBLE | NOT NULL |  | This column contains the internal identification code representing the signature line format. This value is used to join to the signature line format information stored on the SIGN_LINE_FORMAT table. |
| 5 | `SIGN_LINE_EP_R_ID` | DOUBLE | NOT NULL |  | Unique identifier for the signature line to pattern relationship for case integration signature lines. |
| 6 | `STATUS_FLAG` | DOUBLE |  |  | This column contains a flag value representing the result status for which the signature line format is associated. Currently, signature lines can be associated with:2 - Verified and Corrected |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

