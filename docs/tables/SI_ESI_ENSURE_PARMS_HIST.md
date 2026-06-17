# SI_ESI_ENSURE_PARMS_HIST

> This table stores historical information for the ESI_Ensure_Parms table

**Description:** System Integration ESI Ensure Parms History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLERGY_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Allergy_segment_ens_type_cd field from the esi_ensure_parms table |
| 6 | `CODING_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Coding_Segment_Ens_Type_Cd field from the esi_ensure_parms table. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `ENCNTR_ALIAS_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Encntr_alias_ensure_type_cd field from the esi_ensure_parms table. |
| 9 | `ENCNTR_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Encntr_ensure_type_cd field from the esi_ensure_parms table. |
| 10 | `ESI_ENSURE_PARMS_ID` | DOUBLE | NOT NULL |  | Copy of the Esi_ensure_parms_id field from the esi_ensure_parms table. |
| 11 | `ESI_TASK_CD` | DOUBLE | NOT NULL |  | Copy of the Esi_task_cd field from the esi_ensure_parms table. |
| 12 | `EVENT_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Event_ensure_type_cd field from the esi_ensure_parms table. |
| 13 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made new modification on the esi_ensure_parms table |
| 14 | `NK1_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | This ENSURE option provides the ability to override the normal ensure configuration for authenticated persons. For a given transaction, with the Person or Encounter Ensure set to add or update, the processing of authenticated persons do not update the person data in the database. With this option set, if there is an authenticated match found, then the authenticated person will be ensured from the NK1 segment information. The only valid values are UPDATE and 0. |
| 15 | `ORDER_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Order_ensure_type_cd field from the esi_ensure_parms table. |
| 16 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made original modification on the esi_ensure_parms table |
| 17 | `PERSON_ALIAS_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Person_alias_ensure_type_cd field from the esi_ensure_parms table. |
| 18 | `PERSON_ENSURE_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Person_ensure_type_cd field from the esi_ensure_parms table. |
| 19 | `PROBLEM_SEGMENT_ENS_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Problem_segment_ens_type_cd field from the esi_ensure_parms table |
| 20 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Rec_Beg_Eff_Dt_TM field from the esi_ensure_parms table. |
| 21 | `SI_ESI_ENSURE_PARMS_HIST_ID` | DOUBLE | NOT NULL |  | Primary KeyColumn |
| 22 | `UB2_SEGMENT_ENS_TYPE_CD` | DOUBLE |  |  | This ENSURE option provides the ability to specify the ensure configuration for Uniform Billing Data segment. For a given transaction, the ub2 segment ensure will allow UB2 segments to be processed by ESI and post the information received to millennium via ReconcilePatientAndEncounter API provided by registration . The only valid values are REPLACE and 0. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

