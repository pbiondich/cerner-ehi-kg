# ESI_ENSURE_PARMS

> The ESI alias translation table contains information that determines by contributor system and transaction type the add, update and delete privilege for person, encounter, and event data groups.

**Description:** ESI Ensure Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLERGY_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option provides the ability to override the normal encounter ensure configuration. For a given transaction, if the Encounter Ensure would prevent the add or update of encounter data, the allergy segment ensure will override and allow allergy segments (AL1 and ZAL) to be processed. The only valid values are ADD and 0. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CODING_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option provides the ability to override the normal encounter ensure configuration. For a given transaction, if the Encounter Ensure would prevent the add or update of encounter data, the coding segment ensure will override and allow coding segments (DG1, DRG ad PR1) to be processed. The only valid values are ADD and 0. |
| 8 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 9 | `ENCNTR_ALIAS_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option provides the ability to override the normal encounter ensure configuration. For a given transaction, if the Encounter Ensure would prevent the add or update of encounter data, the Encounter Alias Ensure would override and allow a new encounter alias to be added. This ENSURE is used in conjunction with the ALIAS_ENSURE_PARMS_FLAG on the ESI_ALIAS_TRANS table. The only valid values are ADD and 0. |
| 10 | `ENCNTR_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option identifies the database update privilege level for updating encounter data. Examples of these options are: ADD, UPDATE, EXISTS. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `ESI_ENSURE_PARMS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the ESI_ENSURE_PARMS table. |
| 13 | `ESI_TASK_CD` | DOUBLE | NOT NULL |  | ESI task identifies the HL7 trigger event (transaction type) such as Admit, Discharge, Transfer, etc. |
| 14 | `EVENT_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option identifies the database update privilege level for updating event data. Examples of these options are: ADD, UPDATE, REPLACE. |
| 15 | `NK1_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option provides the ability to override the normal ensure configuration for authenticated persons. For a given transaction, with the Person or Encounter Ensure set to add or update, the processing of authenticated persons do not update the person data in the database. With this option set, if there is an authenticated match found, then the authenticated person will be ensured from the NK1 segment information. The only valid values are UPDATE and 0. |
| 16 | `ORDER_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option is used to know when to find and update an order status during clinical event processing. The only valid values are "complete for ORU message" and 0. |
| 17 | `PERSON_ALIAS_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option provides the ability to override the normal person ensure configuration. For a given transaction, if the Person Ensure would prevent the add or update of person data, the Person Alias Ensure would override and allow a new Person alias to be added. This parameter is used in conjunction with the ALIAS_ENSURE_PARMS_FLAG on the ESI_ALIAS_TRANS table. The only valid values are ADD and 0. |
| 18 | `PERSON_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option identifies the database update privilege level for updating person level data. Examples of these options are: ADD, UPDATE, EXISTS. |
| 19 | `PROBLEM_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option provides the ability to override the normal encounter ensure configuration. For a given transaction, if the Encounter Ensure would prevent the add or update of encounter data, the problem segment ensure will override and allow problem segments (PRB) to be processed. The only valid values are ADD and 0. |
| 20 | `UB2_SEGMENT_ENS_TYPE_CD` | DOUBLE |  |  | This ENSURE option provides the ability to specify the ensure configuration for Uniform Billing Data segment. For a given transaction, the ub2 segment ensure will allow UB2 segments to be processed by ESI and post the information received to millennium via ReconcilePatientAndEncounter API provided by registration . The only valid values are REPLACE and 0. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |

