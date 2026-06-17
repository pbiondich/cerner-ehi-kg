# RX_CLAIM

> Table used to store the claims information.

**Description:** Rx Claim  
**Table type:** ACTIVITY  
**Primary key:** `RX_CLAIM_ID`  
**Columns:** 51  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_IDENT_TXT` | VARCHAR(50) | NOT NULL |  | Unique identifier of activity within a claim/prior request. |
| 3 | `ADDL_DRUG_IDENT_VALUE_TXT` | VARCHAR(255) |  |  | Identifies a drug other than NDC that is required for non-US clients to send in as part of a claim. |
| 4 | `ATTACHMENT_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Stores the Long_blob_id of the attachment blob data attached during a transaction |
| 5 | `ATTACHMENT_NAME` | VARCHAR(100) | NOT NULL |  | Stores the name of the attachment file sent during a transaction |
| 6 | `AUTHORIZATION_IDENT_TXT` | VARCHAR(50) | NOT NULL |  | This column holds the value of pre-generated authorization ID that will be sent for pharmacy prior request transactions. The unique identifier assigned by the health provider to identify the Authorization; must be globally unique and start with EncounterFacilityID followed by a unique identifier assigned by the facility information system, followed by date/time of the transaction. |
| 7 | `AUTHORIZATION_NBR_TXT` | VARCHAR(50) |  |  | Authorization number for claims |
| 8 | `CARD_HOLDER_IDENT` | VARCHAR(100) | NOT NULL |  | The member number of the subscriber to the health plan. |
| 9 | `CLAIM_FORMAT_CD` | DOUBLE | NOT NULL |  | Format used in building the Message string, containing the claims information, that is sent in the transaction. |
| 10 | `CLAIM_FORMAT_TYPE_CD` | DOUBLE | NOT NULL |  | Claim Format type cd |
| 11 | `CLAIM_SEQ` | DOUBLE |  |  | When multiple claims are submitted in one transaction, sequence indicates the position of a particular claim within the transaction. |
| 12 | `CLAIM_STATUS_CD` | DOUBLE | NOT NULL |  | Status of claim |
| 13 | `CLAIM_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Message string containing claims information that is sent in the transaction. |
| 14 | `CLAIM_TRANS_CD` | DOUBLE | NOT NULL |  | Type of claims transaction. |
| 15 | `COMMENT_CD` | DOUBLE | NOT NULL |  | Stores the Code value of the Predefined comment from Reason codes codeset# 4031 (with event type of Internal Complaint) |
| 16 | `COMMENT_TXT_ID` | DOUBLE | NOT NULL | FK→ | stores the long_text_id of the free textComment entered by user in Internal complaint, Upto 1000 Characters need to be supported |
| 17 | `COPAY_AMT` | DOUBLE | NOT NULL |  | Copay amount of dispense transaction |
| 18 | `DENIED_CD` | DOUBLE | NOT NULL |  | Stores the code value of Denied Code that came back during a prior authorization response from payer |
| 19 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | dispense hx id |
| 20 | `DUR_IND` | DOUBLE |  |  | This field indicates the presence of DUR (Drug Utilization Review) information in the response record from the Health Plan (i.e. Medicaid). This piece of the response record contains various Health Plan specific information with regards to the drug prescribed. The DUR information is only returned within a Claim Process. |
| 21 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Health Plan ID |
| 22 | `LEVEL5_CD` | DOUBLE | NOT NULL |  | Location of the Workstation (PC) that was used in filling the prescription. |
| 23 | `MANUAL_ADJUDICATED_IND` | DOUBLE | NOT NULL |  | Indicates whether the adjudication is manual or electronic. 0 - Electronic, 1 - Manual |
| 24 | `MANUAL_OVERRIDE_AUTH_NAME` | VARCHAR(250) |  |  | Free Text name of the personnel who authorized manual override |
| 25 | `MANUAL_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Indicates whether user manually overrode the claim status or not. 0 - No manual override 1 - Manual override |
| 26 | `MANUAL_OVERRIDE_NOTE_TXT` | VARCHAR(250) |  |  | Any additional notes related to manual override entered by the user. |
| 27 | `MANUAL_OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Reason for the manual override. |
| 28 | `ORIG_CLAIM_STATUS_CD` | DOUBLE | NOT NULL |  | Status of claim on previous attempt. Applicable only when a claim submission is attempted more than once. |
| 29 | `PRE_OVERRIDE_CLAIM_STATUS_CD` | DOUBLE |  |  | Claim status that was received from the switch before the status was automatically overridden by the system |
| 30 | `PRINT_FLAG` | DOUBLE | NOT NULL |  | Determines whether rejected Claim Labels should print or not. |
| 31 | `REIMBURSEMENT_AMT` | DOUBLE | NOT NULL |  | Reimbursement amount for this dispense transaction |
| 32 | `RESEND_ACTIVITY_IDENT_TXT` | VARCHAR(50) | NOT NULL |  | Stores the activity_ident_txt for the activities to be resent under new prior-request authorization transaction |
| 33 | `RESEND_AUTH_IDENT_TXT` | VARCHAR(50) | NOT NULL |  | Stores the authorization_ident_txt under which the Activities will be resent for Prior request authorization transaction |
| 34 | `RESEND_ORDERED_DT_TM` | DATETIME |  |  | Stores the date and time for resending the activities(orders) under new prior request authorization transaction |
| 35 | `RESEND_ORDERED_TZ` | DOUBLE | NOT NULL |  | Stores the time zone in which the ordered_dt will be sent for resend prior request authorization transaction |
| 36 | `RESPONSE_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Message string containing response fort he submitted claim transaction. |
| 37 | `RX_CLAIM_ID` | DOUBLE | NOT NULL | PK | Unique ID per claim |
| 38 | `SKIP_COB_REASON_CD` | DOUBLE | NOT NULL |  | Reason for skipping the Coordination of Benefit process. |
| 39 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | Location of the pharmacy that filled the prescription. |
| 40 | `SWITCH_CD` | DOUBLE | NOT NULL |  | Switch to which the claim transaction was sent. |
| 41 | `SYSTEM_ERROR_CD` | DOUBLE | NOT NULL |  | DO NOT USE - use system_err_cd instead |
| 42 | `SYSTEM_ERR_CD` | DOUBLE | NOT NULL |  | Error, if any, encountered during claim submission. |
| 43 | `TRANSACTION_NBR` | DOUBLE | NOT NULL |  | Stores the auto generated ID of a HAAD Transaction that happens on an authorization. This will be non-unique as multiple claim records can share a single transaction_id. Value from sequence rx_claim_seq |
| 44 | `TRANS_DT_TM` | DATETIME |  |  | Date this transaction was created. |
| 45 | `TRANS_TZ` | DOUBLE | NOT NULL |  | Time zone for the claim transaction |
| 46 | `UNCLAIMED_IND` | DOUBLE |  |  | Identifies if this claim was ever in an unclaimed status. |
| 47 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTACHMENT_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `CLAIM_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `COMMENT_TXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `RESPONSE_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RXA_ORD_DISP_HP_OBS_ST](RXA_ORD_DISP_HP_OBS_ST.md) | `RXA_CLAIM_ID` |
| [RX_CLAIM_RESPONSE](RX_CLAIM_RESPONSE.md) | `RX_CLAIM_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `OP_RX_CLAIM_ID` |

