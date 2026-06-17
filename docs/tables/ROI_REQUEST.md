# ROI_REQUEST

> Stores request information such as request type, request reason, requester type, requester id, etc for ROI Request row

**Description:** Stores Request for Medical record information (i.e. request for patient chart).  
**Table type:** ACTIVITY  
**Primary key:** `ROI_REQUEST_ID`  
**Columns:** 59  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPROVAL_IND` | DOUBLE |  |  | This is an indicator the is valued when a request needing approval is approved. *****This column is not being used |
| 6 | `AUTHORIZATION_FLAG` | DOUBLE | NOT NULL |  | Identifies if a request has been authorization. Flag values 1- Authorized; 2- Not Authorized; 3- Implied Consent |
| 7 | `AUTHORIZED_IND` | DOUBLE |  |  | Indicates if we have an authorization to fill this request |
| 8 | `AUTHORIZED_NEEDED_IND` | DOUBLE |  |  | The indicator of authorized needed |
| 9 | `AUTHORIZED_REJECT_REASON_CD` | DOUBLE | NOT NULL |  | This is the code value for the authorize reject reason |
| 10 | `BATCH_IND` | DOUBLE |  |  | This field is used to show if this request is a batch request ****This column is not being used |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BILLABLE_IND` | DOUBLE |  |  | Indicates if this request is billable |
| 13 | `BILL_TO_ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier to the address table |
| 14 | `BILL_TO_ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | CODE SET:212 The address type is the code set value which identifies the type of address for the address row (i.e., home, business, etc.) |
| 15 | `BILL_TO_ADDRESS_TYPE_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the priority or precedence that one address row has over another when both address rows contain the same parent_entity_name, parent_entity_id, and address_type_cd with the same meaning. |
| 16 | `BILL_TO_FAX_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the phone table, identifies the fax number associated with the bill to address. |
| 17 | `BILL_TO_PHONE_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier to the phone table, it identifies the phone number associated with the bill to address |
| 18 | `CANCEL_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who cancelled the request.This is the value of the unique primary identifier of the personnel table. It is an internal system assigned number. ***This column is not being used |
| 19 | `CHARGES_PER_PAGE` | DOUBLE |  |  | Charges per page |
| 20 | `CHART_REQUEST_ID` | DOUBLE | NOT NULL |  | Identifies the chart request that was created when documents are printed via MRP |
| 21 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who created the request.This is the value of the unique primary identifier of the personnel table. It is an internal system assigned number. *** This column isnot being used |
| 22 | `DELIVERY_METHOD_CD` | DOUBLE | NOT NULL |  | This is the method of delivery that will be used. |
| 23 | `DISCLOSURE_IND` | DOUBLE | NOT NULL |  | disclosure indicator |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `EXPECTED_TURN_AROUND` | DOUBLE |  |  | expected turn around |
| 26 | `HIM_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The primary key of him_request table |
| 27 | `LAST_UPDATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who last updated the request.This is the value of the unique primary identifier of the personnel table. It is an internal system assigned number. *** This column is not being used |
| 28 | `MAIL_TO_ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier to the address table |
| 29 | `MAIL_TO_ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | CODE SET:212 The address type is the code set value which identifies the type of address for the address row (i.e., home, business, etc.) |
| 30 | `MAIL_TO_ADDRESS_TYPE_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the priority or precedence that one address row has over another when both address rows contain the same parent_entity_name, parent_entity_id, and address_type_cd with the same meaning. |
| 31 | `MAIL_TO_FAX_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier to the phone table, it identifies the fax number associated with the mail to address |
| 32 | `MAIL_TO_PHONE_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier to the Phone table that identifies the phone number to be associated with the mail to address. |
| 33 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 34 | `PREBILL_IND` | DOUBLE |  |  | The indicator of pre-bill |
| 35 | `PREBILL_OVER_AMOUNT` | DOUBLE |  |  | Pre-bill over amount |
| 36 | `PREBILL_OVER_IND` | DOUBLE |  |  | The indicator of pre-bill over |
| 37 | `REJECTED_REASON_CD` | DOUBLE | NOT NULL |  | This is the reason that the request was rejected *** This column is not being used |
| 38 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CR_REPORT_REQUEST table. It is an internal system assigned number. |
| 39 | `REQUESTER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. *** This column is not being used |
| 40 | `REQUESTER_SOURCE_CD` | DOUBLE | NOT NULL |  | requester source code |
| 41 | `REQUESTER_TYPE_CD` | DOUBLE | NOT NULL |  | Requester source such as Health care institution, Physician,attorney, or patient *** This column is not being used |
| 42 | `REQUEST_DT_TM` | DATETIME |  |  | The Date and Time that the request was entered *** This column is not being used |
| 43 | `REQUEST_NUMBER` | DOUBLE |  |  | This is a unique number that will be used by the user to reference the request *** This column is not being used |
| 44 | `REQUEST_NUMBER_POOL_CD` | DOUBLE | NOT NULL |  | request number pool code identifies a unique set or list of request identifiers (I.e., numbers). The request number pool code also determines the accept/display format for the unique set of identifiers. *** This column is not being used |
| 45 | `REQUEST_PARENT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the requester table. It is an internal system assigned number.This identifies of the parent batch request. *** This column is not being used |
| 46 | `REQUEST_REASON_CD` | DOUBLE | NOT NULL |  | The reason the request was made such as Subpoenas, court order, further medical care |
| 47 | `REQUEST_STATUS_CD` | DOUBLE | NOT NULL |  | This is the status of the request. (i.e. Canceled, completed or hold) *** This column is not being used |
| 48 | `REQUEST_STATUS_DT_TM` | DATETIME |  |  | This is the date and time that the status was set/changed *** This column is not being used |
| 49 | `REQUEST_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person id of the person who is requesting this information *** This column is not being used |
| 50 | `REQUEST_TYPE_CD` | DOUBLE | NOT NULL |  | This is the type of request. (i.e. Patient care, ROI, committee) *** This column is not being used |
| 51 | `REQUIRED_DT_TM` | DATETIME |  |  | This is the date and time that the requester is wanting the request to be completed *** This column is not being used |
| 52 | `ROI_REQUESTER_ID` | DOUBLE | NOT NULL | FK→ | .This is the value of the unique primary identifier of the personnel table. It is an internal system assigned number. *** This column is not being used |
| 53 | `ROI_REQUEST_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the Roi request table. It is an internal system assigned number |
| 54 | `TO_LOCATION_CD` | DOUBLE | NOT NULL |  | This is the location that the request should be delivered to. *** This column is not being used |
| 55 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 58 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 59 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_TO_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `BILL_TO_FAX_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `BILL_TO_PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `HIM_REQUEST_ID` | [HIM_REQUEST](HIM_REQUEST.md) | `HIM_REQUEST_ID` |
| `MAIL_TO_ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `MAIL_TO_FAX_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `MAIL_TO_PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |
| `REQUESTER_ID` | [REQUESTER](REQUESTER.md) | `REQUESTER_ID` |
| `REQUEST_PARENT_ID` | [REQUESTER](REQUESTER.md) | `REQUESTER_ID` |
| `ROI_REQUESTER_ID` | [REQUESTER](REQUESTER.md) | `REQUESTER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [REQUEST_EVENT_RELTN](REQUEST_EVENT_RELTN.md) | `ROI_REQUEST_ID` |
| [ROI_REJECT_REASON](ROI_REJECT_REASON.md) | `ROI_REQUEST_ID` |

