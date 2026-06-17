# REQUESTER

> This is table is used to identify the ROI requesters.This table has requester specific fields such as billable ind, prebill, delivery method...

**Description:** Requester  
**Table type:** REFERENCE  
**Primary key:** `REQUESTER_ID`  
**Columns:** 46  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPROVAL_IND` | DOUBLE |  |  | This indicates if a request has bee approved |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILLABLE_IND` | DOUBLE |  |  | this indicates if the request is billable |
| 8 | `BILL_TO_ADDRESS_CD` | DOUBLE |  |  | The address type code that the bill will be sent to |
| 9 | `BILL_TO_ADDRESS_ID` | DOUBLE |  | FK→ | This is the unique key to the address table. |
| 10 | `BILL_TO_ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | bill to address type code |
| 11 | `BILL_TO_ADDRESS_TYPE_SEQ` | DOUBLE | NOT NULL |  | bill to address type sequence |
| 12 | `BILL_TO_FAX_ID` | DOUBLE |  | FK→ | This is the unique key to the Phone table |
| 13 | `BILL_TO_PHONE_ID` | DOUBLE |  | FK→ | This the Phone number associated with the bill to address. It is the unique identifier to the phone table |
| 14 | `CHARGES_PER_PAGE` | DOUBLE |  |  | This is the charges per page to be billed |
| 15 | `DELIVERY_METHOD_CD` | DOUBLE |  |  | This is the delivery method |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `EXPECTED_TURN_AROUND` | DOUBLE |  |  | This is the expected turn around time |
| 18 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 19 | `MAIL_TO_ADDRESS_CD` | DOUBLE |  |  | This is the address type that the request will be mailed to |
| 20 | `MAIL_TO_ADDRESS_ID` | DOUBLE |  | FK→ | This is the unique identifier to the address table |
| 21 | `MAIL_TO_ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | mail to address type code |
| 22 | `MAIL_TO_ADDRESS_TYPE_SEQ` | DOUBLE | NOT NULL |  | mail to address type sequence |
| 23 | `MAIL_TO_FAX_ID` | DOUBLE |  | FK→ | This is the fax phone number associated with the mail to address. This is the unique identifier to the phone table |
| 24 | `MAIL_TO_PHONE_ID` | DOUBLE |  | FK→ | This is the phone number that is associated with the mail to address. It is the unique identifier to the Phone table. |
| 25 | `NAME_FIRST` | VARCHAR(100) |  |  | This column is the first name for a requester or if the requester is an organization then it is the organization name. |
| 26 | `NAME_FIRST_KEY` | VARCHAR(100) |  |  | This column is the first name for a requester all capitals with punctuation removed. This field is used for indexing and searching for a requester by name. |
| 27 | `NAME_FIRST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_FIRST_KEY_A_NLS column |
| 28 | `NAME_FIRST_KEY_NLS` | VARCHAR(202) |  |  | name first key nls |
| 29 | `NAME_FULL_FORMATTED` | VARCHAR(200) |  |  | This is the complete person name including punctuation and formatting. |
| 30 | `NAME_LAST` | VARCHAR(100) |  |  | This column is the last name for a requester or if the requester is an organization then it is the organization name. |
| 31 | `NAME_LAST_KEY` | VARCHAR(100) |  |  | This column is the last name for a requester or if the requester is an organization then it is the organization name. All capitals with punctuation have been removed. This field is used for indexing and searching for a requester by name. |
| 32 | `NAME_LAST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_LAST_KEY_A_NLS column |
| 33 | `NAME_LAST_KEY_NLS` | VARCHAR(202) |  |  | name last key nls |
| 34 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier of parent entity table |
| 35 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | Name of the parent entity table |
| 36 | `PREBILL_IND` | DOUBLE |  |  | This indicate if the request need to be pre-billed |
| 37 | `PREBILL_OVER_IND` | DOUBLE |  |  | Pre-bill if request bill is over this amount |
| 38 | `REQUESTER_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the requester table. It is an internal system assigned number |
| 39 | `REQUESTER_SOURCE_CD` | DOUBLE |  |  | This is the type of requester(i.e. Attorneys, Insurance Company) |
| 40 | `REQUEST_REASON_CD` | DOUBLE |  |  | The reason the request was made |
| 41 | `SELECTION_CRITERIA_IND` | DOUBLE |  |  | This is the select criteria Indicator |
| 42 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_TO_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `BILL_TO_FAX_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `BILL_TO_PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `MAIL_TO_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `MAIL_TO_FAX_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `MAIL_TO_PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ROI_REQUEST](ROI_REQUEST.md) | `REQUESTER_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `REQUEST_PARENT_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `ROI_REQUESTER_ID` |

