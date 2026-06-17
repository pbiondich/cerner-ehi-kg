# ENCNTR_CARE_MGMT_COMM

> Stores a record of faxes and other communication that were sent from care management solution.

**Description:** Encounter Care Management Communication  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_CARE_MGMT_COMM_ID`  
**Columns:** 29  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTH_NUMBER` | VARCHAR(50) |  |  | The authorization or reference number associated to this fax, saving here in case the authorization row is reused for a new authorization. |
| 2 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | This is the comment for the communication, stored on the long text table. |
| 3 | `COMMUNICATION_STATUS_CD` | DOUBLE | NOT NULL |  | The communication status of the fax such as pending, success or error. |
| 4 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | This is the type of communication that was performed, i.e., fax, phone, website. |
| 5 | `COMPLETE_DT_TM` | DATETIME |  |  | The approximate date and time the sending document is complete. |
| 6 | `CORRESPONDENCE_CD` | DOUBLE | NOT NULL |  | This is the value from a code set 4002584 and denotes the type of correspondence. |
| 7 | `DOCUMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of document transmitted. From code set 4002585. |
| 8 | `ENCNTR_CARE_MGMT_COMM_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated number. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the encounter table. It identifies all the communications for the encounter. |
| 10 | `FT_CONTACT_FAX_TXT` | VARCHAR(50) |  |  | The free-text fax number from the sender for this communication |
| 11 | `FT_CONTACT_NAME` | VARCHAR(100) |  |  | The free-text contact name for this communication. |
| 12 | `FT_CONTACT_PHONE` | VARCHAR(50) |  |  | The free-text phone number for this communication. |
| 13 | `FT_FORMATTED_PHONE_NUMBER` | VARCHAR(100) |  |  | The free text formatted fax number. |
| 14 | `HANDLE_ID` | DOUBLE | NOT NULL | FK→ | Storing a link to the OUTPUTCTX table to retrieve information about outbound faxes status and acknowledgement, to store on this table, before the OUTPUTCTX table is purged. |
| 15 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The health plan that is part of the communication. |
| 16 | `NUMBER_OF_PAGES` | DOUBLE | NOT NULL |  | The number of pages sent. |
| 17 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization the communication is being sent to. |
| 18 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | The output destination identifier that is from output_dest table. It is the device destination for transmitting the fax. |
| 19 | `PHONE_SUFFIX` | VARCHAR(50) |  |  | This field holds the phone number when ad-hoc faxing is used. |
| 20 | `RECIPIENT_NAME` | VARCHAR(100) |  |  | The name of the intended recipient. |
| 21 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the report request from cr_report_request table. |
| 22 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that sent the fax |
| 23 | `SENT_DT_TM` | DATETIME |  |  | Date and time that document was sent. |
| 24 | `TRANSMISSION_STATUS_CD` | DOUBLE | NOT NULL |  | The current RRD transmission status of the document. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_CARE_MGMT_COMM_RLTN](ENCNTR_CARE_MGMT_COMM_RLTN.md) | `ENCNTR_CARE_MGMT_COMM_ID` |

