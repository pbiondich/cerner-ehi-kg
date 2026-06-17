# CONTRACT_PROPERTY

> Contains the contract properties for a given message

**Description:** Contract Property  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_ACTOR1_NAME` | VARCHAR(250) | NOT NULL |  | This identifies the first participant in the acknowledgement process, if applicable. |
| 2 | `ACK_ACTOR2_NAME` | VARCHAR(250) | NOT NULL |  | This identifies the second participant in the acknowledgement process, if applicable. |
| 3 | `ACK_REQUESTED_FLAG` | DOUBLE | NOT NULL |  | This indicates whether a system will return an acknowledgement. Possible values include 1=ALWAYS, 2=PER-MESSAGE, and 0=NEVER |
| 4 | `ACTION_NAME` | VARCHAR(250) | NOT NULL |  | This identifies a process within a service that processes the message. e.g., PRSC_IN040000UK |
| 5 | `ACTION_VERSION_TXT` | VARCHAR(250) | NOT NULL |  | Action version - Alpha-Numeric. |
| 6 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 9 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 10 | `AUTHENTICATION_FLAG` | DOUBLE | NOT NULL |  | Is Authenticated Flag. This determines whether the receiver must identify the sender. Possible values include 0=NONE, 1=TRANSIENT, and 2=PERSISTENT |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `CONTRACT_PROPERTY_ID` | DOUBLE | NOT NULL |  | Primary Key. Unique row identifier. The value for this column will not come from a sequence. The value for the ID will be re-generated nightly as the table contents are reloaded (replaced) |
| 13 | `CPA_IDENT` | VARCHAR(250) | NOT NULL |  | Contract / Property / Action Identifier for parameters governing the exchange of messages between parties. |
| 14 | `DUPLICATE_ELIMINATION_FLAG` | DOUBLE | NOT NULL |  | This field indicates whether the receiver will check for duplicate messages. Possible Values: 0 = NEVER, 1 = ALWAYS, 2 - PER MESSAGE |
| 15 | `DUPLICATE_ELIMINATION_IND` | DOUBLE | NOT NULL |  | Obsolete. Not Used. Column DUPLICATE_ELIMINATION_FLAG will replace this field. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `FROM_PARTYID_TXT` | VARCHAR(250) |  |  | This column contains the information for the FROM PARTYID element of the EBXML wrapper. |
| 18 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization. It identifies the service. |
| 19 | `PARTY_KEY_TXT` | VARCHAR(250) | NOT NULL |  | Identifies a business service within an organization, which could be in the form of OCS-Instance, e.g., D81001-811. |
| 20 | `PAYLOAD_ENCODING_TXT` | VARCHAR(250) |  |  | This column contains the information for the PAYLOAD ENCODING element of the EBXML wrapper. |
| 21 | `PAYLOAD_STYLE_TXT` | VARCHAR(250) |  |  | This column contains the information for the PAYLOAD STYLE element of the EBXML wrapper. |
| 22 | `PAYLOAD_VER_TXT` | VARCHAR(250) |  |  | This column contains the information for the PAYLOAD VERSION element of the EBXML wrapper. |
| 23 | `PERSIST_DURATION_NBR` | DOUBLE | NOT NULL |  | This is the minimum length of time that data from a reliably sent message is kept in persistent storage by a receiving system. (seconds) |
| 24 | `RETRIES_NBR` | DOUBLE | NOT NULL |  | This is the maximum number of times a sending system should attempt to redeliver an unacknowledged message. |
| 25 | `RETRY_INTERVAL_NBR` | DOUBLE | NOT NULL |  | This is the time a sending system will wait before retrying (seconds) |
| 26 | `SCHEMA_LOCATION_TXT` | VARCHAR(250) | NOT NULL |  | Schema LocationColumn |
| 27 | `SEND_URL` | VARCHAR(250) | NOT NULL |  | This identifies the address of the receiving system |
| 28 | `SERVICE_NAME` | VARCHAR(250) | NOT NULL |  | Service NameColumn |
| 29 | `SLA_IND` | DOUBLE | NOT NULL |  | Service Level Agreement. This indicates whether the message requires SLA. |
| 30 | `SYNC_REPLY_MODE_FLAG` | DOUBLE | NOT NULL |  | This indicates that the sender expects a synchronous response. Possible values include: 1 = MSHSIGNALSONLY; 2=SIGNALSONLY; 3=RESPONSEONLY; 4=SIGNALSANDRESPONSE; and 0=none. |
| 31 | `TIMEOUT_NBR` | DOUBLE | NOT NULL |  | Determine the amount of time our system will await a response over a communication line. |
| 32 | `TO_PARTYID_TXT` | VARCHAR(250) |  |  | This column contains the information for the TO PARTYID element of the EBXML wrapper. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 38 | `XLINK_HREF_TXT` | VARCHAR(250) |  |  | This column contains the information for the XLINK HREF element of the EBXML wrapper. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

