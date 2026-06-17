# RX_CLAIM_AUTH_AUDIT

> Table used to audit asynchronized transactions for Claim Authorization services

**Description:** Pharmacy Claim Authorization Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the action for which the audit row is entered. |
| 2 | `AUTHORIZATION_IDENT_TXT` | VARCHAR(100) | NOT NULL |  | This column holds the value of pre-generated authorization ID that will be sent for pharmacy prior request transactions. The unique identifier assigned by the health provider to identify the Authorization; must be globally unique and start with EncounterFacilityID followed by a unique identifier assigned by the facility information system, followed by date/time of the transaction. |
| 3 | `CONTRIBUTOR_SYSTEM_TXT` | VARCHAR(5) | NOT NULL |  | Identifies the subsystem that entered this row. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Identifies date & time the row was created. |
| 5 | `MESSAGE_TXT` | VARCHAR(1000) | NOT NULL |  | Text indicating success or failure message |
| 6 | `RX_CLAIM_AUTH_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the claim_authorization_audit table. |
| 7 | `SUCCESS_IND` | DOUBLE | NOT NULL |  | Indicates if the claim was processed successfully. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

