# PFT_AP_REFUND

> Holds Accounts Payable refund information.

**Description:** PFT AP REFUND  
**Table type:** ACTIVITY  
**Primary key:** `PFT_AP_REFUND_ID`  
**Columns:** 37  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | Address of the entity receiving the refund. |
| 6 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason the refund was cancelled. |
| 7 | `CERTIFICATE_NBR` | VARCHAR(100) |  |  | Certificate Number |
| 8 | `EMPLOYER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the employer. |
| 9 | `EMPLOYER_NAME` | VARCHAR(255) |  |  | Name of the employer. |
| 10 | `EXPEDITED_IND` | DOUBLE | NOT NULL |  | Refund applied immediately, 0 = False 1 = True |
| 11 | `GUAR_ACCT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated account number for the guarantor(s) associated to the patient which identifies the unique record in the account table. |
| 12 | `INS_COMPANY_IDENT` | VARCHAR(100) |  |  | The insurance company identifier for a specific insurance company associated to the insurance refund |
| 13 | `INS_GROUP_NUMBER_TXT` | VARCHAR(50) |  |  | The group number of the insurance company associated to the insurance refund |
| 14 | `PARENT_PFT_AP_REFUND_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row for the amount indicating the pending refund amount for the payment detail. |
| 15 | `PATIENT_NAME` | VARCHAR(255) |  |  | Name of the patient related to the refund. |
| 16 | `PFT_AP_REFUND_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the table. |
| 17 | `PHONE_ID` | DOUBLE | NOT NULL | FK→ | Phone ID is the primary unique identification number of the phone table. It is an internal system assigned sequence number. |
| 18 | `POSTED_IND` | DOUBLE |  |  | This indicator shows whether the refund has been posted or not. |
| 19 | `RECEIVING_NAME` | VARCHAR(255) |  |  | Name of the person receiving the refund. |
| 20 | `REFERENCE_IDENT` | VARCHAR(255) |  |  | Unique identifier to link a refund to corresponding information received from payer. |
| 21 | `REFUND_AMT` | DOUBLE |  |  | The amount of the refund. |
| 22 | `REFUND_CURR_CD` | DOUBLE | NOT NULL |  | Currency code of the refund. |
| 23 | `REFUND_DT_TM` | DATETIME |  |  | Date of the refund. |
| 24 | `REFUND_METHOD_FLAG` | DOUBLE | NOT NULL |  | Identifies the method by which the refund will be made. 0 = AP refund; 1 = Credit Card Refund |
| 25 | `REFUND_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason that the refund was created. |
| 26 | `REFUND_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the refund. |
| 27 | `REFUND_TYPE_FLAG` | DOUBLE |  |  | The type of the refund. |
| 28 | `RESPONSIBLE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who is responsible for this refund. It will normally be the original creator of the refund but could also be someone who modified a previously denied refund. |
| 29 | `SPONSOR_ID` | DOUBLE | NOT NULL |  | Unique identifier of the sponsor. |
| 30 | `SPONSOR_NAME` | VARCHAR(255) |  |  | Name of the sponsor. |
| 31 | `TRANS_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Transaction alias that is used for posting the refund. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `VENDOR_NUMBER` | VARCHAR(50) |  |  | Client defined reference string for the Vendor sending the refund. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `EMPLOYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `GUAR_ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `PARENT_PFT_AP_REFUND_ID` | [PFT_AP_REFUND](PFT_AP_REFUND.md) | `PFT_AP_REFUND_ID` |
| `PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `RESPONSIBLE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRANS_ALIAS_ID` | [PFT_TRANS_ALIAS](PFT_TRANS_ALIAS.md) | `PFT_TRANS_ALIAS_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PFT_AP_REFUND](PFT_AP_REFUND.md) | `PARENT_PFT_AP_REFUND_ID` |
| [PFT_AP_REFUND_HIST](PFT_AP_REFUND_HIST.md) | `PFT_AP_REFUND_ID` |
| [PFT_AP_REFUND_RELTN](PFT_AP_REFUND_RELTN.md) | `PFT_AP_REFUND_ID` |
| [PFT_AP_REFUND_RETURN_INFO](PFT_AP_REFUND_RETURN_INFO.md) | `PFT_AP_REFUND_ID` |

