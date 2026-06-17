# UKRWH_CDS_ORG_NACS

> Contains Reference Descriptions for NHS NACS Organisations.

**Description:** UK Reporting Warehouse Comm Data Set Org National Administrative Code Service  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 7 | `IT_CLUSTER_NACS` | VARCHAR(3) |  |  | LO - LOCAL SERVICE PROVIDER (LSP) |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 9 | `LINE1_ADDR` | VARCHAR(35) |  |  | The first text string comprising one line of an ADDRESS. |
| 10 | `LINE2_ADDR` | VARCHAR(35) |  |  | The second text string comprising one line of an ADDRESS. |
| 11 | `LINE3_ADDR` | VARCHAR(35) |  |  | The third text string comprising one line of an ADDRESS. |
| 12 | `LINE4_ADDR` | VARCHAR(35) |  |  | The fourth text string comprising one line of an ADDRESS. |
| 13 | `LINE5_ADDR` | VARCHAR(35) |  |  | The fifth text string comprising one line of an ADDRESS. |
| 14 | `ORGANISATION_NAME` | VARCHAR(100) |  |  | The name by which an ORGANISATION wishes to be known or the official name given to an ORGANISATION. |
| 15 | `ORGANISATION_NAME_UNF` | VARCHAR(100) |  |  | This organization name in all capitals with punctuation removed. This field is used for indexing and searching for a organization by name. |
| 16 | `ORGANISATION_TYPE` | VARCHAR(50) |  |  | A list of ORGANISATION TYPES of ORGANISATIONS according to the nature of the ORGANISATION (e.g. NHS Trust, Health Authority etc.). |
| 17 | `ORGANIZATION_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 18 | `ORG_CODE_NACS` | VARCHAR(8) |  |  | The code by which an ORGANISATION wishes to be known or the official code given to an ORGANISATION. |
| 19 | `POSTCODE` | VARCHAR(25) |  |  | The code allocated by the Post Office to identify a group of postal delivery points. A code used primarily for the delivery of correspondence to ADDRESSES. POSTCODES may also be used to define a GEOGRAPHIC AREA. |
| 20 | `SHA_NACS` | VARCHAR(3) |  |  | Strategic Health Authority is an ORGANISATION. An NHS organisation established to lead the strategic development of the local health service and manage Primary Care Trusts and NHS Trusts on the basis of local accountability agreements. |
| 21 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 22 | `UKRWH_CDS_ORG_NACS_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds org nacs table. It is an internal system assigned number. |
| 23 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

