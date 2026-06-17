# EEM_RX_ELIG_DETAIL

> The EEM_RX_ELIG_DETAIL table stores summary data for prescription eligibility transactions.

**Description:** EEM Prescription Eligibility Detail  
**Table type:** ACTIVITY  
**Primary key:** `EEM_RX_ELIG_DETAIL_ID`  
**Columns:** 58  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIN` | VARCHAR(50) |  |  | Bank Identification Number used as additional identification for the patient from the inbound message. This a primary identifier to drive billing of a claim. |
| 2 | `CARDHOLDER_IDENT` | VARCHAR(50) |  |  | The prescription plan ID that is on the prescription plan card. |
| 3 | `CARDHOLDER_NAME` | VARCHAR(80) |  |  | Cardholder's last name, first name from the inbound message. |
| 4 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 5 | `COPAY_LIST_KEY` | VARCHAR(50) |  |  | Co-pay code is a key to the formulary and benefits data for a pharmacy benefits manager from the inbound message. |
| 6 | `COVERAGE_LIST_KEY` | VARCHAR(50) |  |  | Coverage code is a key to the formulary and benefits data for a pharmacy benefits manager from the inbound message. |
| 7 | `DATA_EXPIRE_DT_TM` | DATETIME |  |  | Date and time that the data expires. |
| 8 | `EEM_RX_ELIG_DETAIL_ID` | DOUBLE | NOT NULL | PK | Primary identifier of EEM_RX_ELIG_DETAIL table. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the encounter tied to this transaction. |
| 10 | `FORMULARY_ALT_LIST_KEY` | VARCHAR(50) |  |  | Alternate formulary code is a key to the formulary and benefits data for a pharmacy benefits manager from the inbound message. |
| 11 | `FORMULARY_LIST_KEY` | VARCHAR(50) |  |  | Formulary code is a key to the formulary and benefits data for a pharmacy benefits manager from the inbound message. |
| 12 | `GROUP_IDENT` | VARCHAR(50) |  |  | Group Identification number from the inbound message. |
| 13 | `GROUP_NAME` | VARCHAR(80) |  |  | Group name from the inbound message. |
| 14 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the health plan used with this transaction. |
| 15 | `IB_ADDRESS_LINE_1` | VARCHAR(55) |  |  | Person's address line 1 from the inbound message. |
| 16 | `IB_ADDRESS_LINE_2` | VARCHAR(55) |  |  | Person's address line 2 from the inbound message. |
| 17 | `IB_BIRTH_DT_TM_TXT` | VARCHAR(10) |  |  | Person's birth date and time from the inbound message. |
| 18 | `IB_CITY` | VARCHAR(30) |  |  | Person's city from the inbound message. |
| 19 | `IB_FIRST_NAME` | VARCHAR(35) |  |  | Person's given first name from the inbound message. |
| 20 | `IB_GENDER_CD` | DOUBLE | NOT NULL |  | Person's gender that from the inbound message. |
| 21 | `IB_LAST_NAME` | VARCHAR(60) |  |  | Person's given last name from the inbound message. |
| 22 | `IB_MIDDLE_NAME` | VARCHAR(25) |  |  | Person's given middle name from the inbound message. |
| 23 | `IB_NAME_SUFFIX` | VARCHAR(10) |  |  | Person's given name suffix from the inbound message. |
| 24 | `IB_PAT_CHANGE_IND` | DOUBLE | NOT NULL |  | This captures the change indicator field from the inbound eligibility response for the patient. If set, the payer's version of the patient's demographics data is different from what was sent outbound. |
| 25 | `IB_POSTAL_CODE` | VARCHAR(15) |  |  | Person's postal Code (Zip Code) from the inbound message. |
| 26 | `IB_SSN` | VARCHAR(30) |  |  | Person's Social Security Number from the inbound message. |
| 27 | `IB_STATE` | VARCHAR(2) |  |  | Person's state from the inbound message. |
| 28 | `INTERCHANGE_CONTROL_NBR_IDENT` | VARCHAR(9) |  |  | A control number assigned by the interchange sender as a means to identify a transaction from the sender's system. |
| 29 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Primary identifier for a transaction. |
| 30 | `OB_BIRTH_DT_TM_TXT` | VARCHAR(35) |  |  | Person's birth date and time from the outbound message. |
| 31 | `OB_FIRST_NAME` | VARCHAR(35) |  |  | Person's given first name from the outbound message. |
| 32 | `OB_GENDER_CD` | DOUBLE | NOT NULL |  | Person's gender from the outbound message. |
| 33 | `OB_LAST_NAME` | VARCHAR(60) |  |  | Person's given last name from the outbound message. |
| 34 | `OB_MIDDLE_NAME` | VARCHAR(25) |  |  | Person's given middle name from the outbound message. |
| 35 | `OB_POSTAL_CODE` | VARCHAR(15) |  |  | Person's postal Code (Zip Code) from the outbound message. |
| 36 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 37 | `PATIENT_UNIT_NUMBER` | VARCHAR(50) |  |  | Identification number that can be used in conjunction with the member id for better identifying dependents or non-uniquely identifiable members of a plan. |
| 38 | `PBM_MEMBER_IDENT` | VARCHAR(80) |  |  | Identifier used by the payer to uniquely identify the person. |
| 39 | `PBM_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the carrier organization used with this transaction. |
| 40 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the person for who this transaction was sent. |
| 41 | `PLAN_ADMIN_IDENT` | VARCHAR(80) |  |  | This further identifies the plan administrator within the contributor system. |
| 42 | `PLAN_ADMIN_NAME` | VARCHAR(60) |  |  | Name of the prescription health plan administrator or payer. |
| 43 | `PRESCRIBER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the patient's prescribing provider. |
| 44 | `PRESCRIPTION_PLAN_IDENT` | VARCHAR(50) |  |  | Prescription health plan identification number from the inbound message. |
| 45 | `PRESCRIPTION_PLAN_NAME` | VARCHAR(80) |  |  | Prescription health plan name from the inbound message. |
| 46 | `PROCESS_CONTROL_NUMBER` | VARCHAR(80) |  |  | The Processor Control Number (PCN) is a secondary identifier to the BIN that may be used in routing of pharmacy transactions. A PBM/processor/plan may choose to differentiate different plans/benefit packages with the use of unique PCNs. The PCN is defined by the PBM/processor. |
| 47 | `REPLY_DT_TM` | DATETIME |  |  | Date and time the transaction was returned. |
| 48 | `RX_HIST_VERSION_CD` | DOUBLE | NOT NULL |  | Defines the specification version to be utilized for the transaction to request a person's prescription history. |
| 49 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person who is the sender of the transaction. |
| 50 | `SENT_DT_TM` | DATETIME | NOT NULL |  | Date and time the transaction was sent outbound. |
| 51 | `SEQUENCE` | DOUBLE | NOT NULL |  | Used to locate the proper ST to SE loop when looking up the original inbound message via the long_blob table. |
| 52 | `TRANS_DATA_CD` | DOUBLE | NOT NULL |  | Describes the high level status of a transaction message based on the system's business rules. The message may be in a pending, error, or returned state. |
| 53 | `TRANS_VENUE_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the type of transaction and the venue from where it was submitted. |
| 54 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PBM_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRESCRIBER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EEM_ELIG_SVC_DETAIL](EEM_ELIG_SVC_DETAIL.md) | `EEM_RX_ELIG_DETAIL_ID` |
| [EEM_RX_MED_HIST_DETAIL](EEM_RX_MED_HIST_DETAIL.md) | `EEM_RX_ELIG_DETAIL_ID` |

