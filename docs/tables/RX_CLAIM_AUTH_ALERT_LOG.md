# RX_CLAIM_AUTH_ALERT_LOG

> Table used to record error and warnig messagess for authorization alerts to HAAD

**Description:** Pharmacy Claim Authorization Alert Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDL_REFERENCE_TXT` | VARCHAR(150) | NOT NULL |  | Reference pertaining to the object that has warning or error associated. |
| 2 | `ALERT_CD` | DOUBLE | NOT NULL |  | Field will house code value representing ALERT_IDENT_TXT from code set 4003364 and 4003365. |
| 3 | `ALERT_IDENT_TXT` | VARCHAR(12) | NOT NULL |  | Contains an alert identifier from a foreign system. |
| 4 | `AUTHORIZATION_IDENT_TXT` | VARCHAR(100) | NOT NULL |  | This column holds the value of pre-generated authorization ID that will be sent for pharmacy prior request transactions. The unique identifier assigned by the health provider to identify the Authorization; must be globally unique and start with EncounterFacilityID followed by a unique identifier assigned by the facility information system, followed by date/time of the transaction.Authorization identifier for multiple claim/activity rows in rx_claim table. |
| 5 | `FIELD_NAME` | VARCHAR(50) | NOT NULL |  | The field of the object that has warning or error associated |
| 6 | `FIELD_VALUE` | VARCHAR(50) | NOT NULL |  | Value that was set in the field identified by field column. |
| 7 | `MESSAGE_TXT` | VARCHAR(300) | NOT NULL |  | Text explaining the error or warning. |
| 8 | `MESSAGE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies if information is for Error or Warning when any data is received upon upload of the transaction. 0 - Success, 1 - Error, and 2 - Warning |
| 9 | `OBJECT_NAME` | VARCHAR(15) | NOT NULL |  | Identifies if issue is with activity or authorization part or the transaction. |
| 10 | `RX_CLAIM_AUTH_ALERT_LOG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the rx_claim_auth_alert_resp table. |
| 11 | `TRANSACTION_NBR` | DOUBLE | NOT NULL |  | The transaction sequence associated with this authorization. The highest transaction number indicates active transaction for the authorization. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

