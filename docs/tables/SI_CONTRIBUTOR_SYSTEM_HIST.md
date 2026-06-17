# SI_CONTRIBUTOR_SYSTEM_HIST

> This table stores historical information for the Contributor_System table.

**Description:** Contributor System History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACT_CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Copy of the Act_Contributor_System_Cd from the Contributor_system Table |
| 6 | `ALT_CONTRIB_SRC_CD` | DOUBLE | NOT NULL |  | Copy of the Alt_Contrib_Src_Cd from the Contributor_system Table |
| 7 | `AOF_ENABLED_IND` | DOUBLE | NOT NULL |  | When this field is active, the system states that code values will be added on the fly when possible. |
| 8 | `AUTHORIZATION_TYPE_CD` | DOUBLE | NOT NULL |  | The method used for the authorizing messages for this contributor system. |
| 9 | `AUTHORIZATION_URL` | VARCHAR(255) | NOT NULL |  | The URL for authorization information. |
| 10 | `AUTO_COMBINE_IND` | DOUBLE |  |  | Copy of the Auto_Combine_Ind from the Contributor_system Table |
| 11 | `CLIENT_IDENT` | VARCHAR(100) |  |  | Stores the clientId details to contributor_system table. ; Identifies the globally-unique identifier of the client application.; Values are of type UTF8(STRING). Values SHALL not exceed 100 characters in length. |
| 12 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | Copy of the Contributor_Source_CD from the Contributor_system Table |
| 13 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 14 | `CONTR_MODE_CD` | DOUBLE | NOT NULL |  | A description of the workflow that the contributor system is built for (ex: History, Batch, Real-time, etc). |
| 15 | `CONTR_SYS_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Contr_Sys_Type_Cd from the Contributor_system Table |
| 16 | `DISPLAY` | VARCHAR(40) |  |  | Copy of the Display from the Contributor_system Table |
| 17 | `DOC_EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | Copy of the Doc_Event_Class_Cd from the Contributor_system Table |
| 18 | `ENHANCED_PROCESSING_CD` | DOUBLE | NOT NULL |  | Additional processing occurs when this value is set |
| 19 | `ESI_LOG_BITMAP` | DOUBLE | NOT NULL |  | This field defines the interaction between the ESI_LOG and LONG_BLOB tables for messages generated through the ESI Java server. |
| 20 | `ESI_ORG_ALIAS_CD` | DOUBLE | NOT NULL |  | Copy of the Esi_Org_Alias_Cd from the Contributor_system Table |
| 21 | `ESI_SPECIAL_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Copy of Esi_special_source_flag from the contributor_system table |
| 22 | `ESO_SPECIAL_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Copy of Eso_special_source_flag from the contributor_system table |
| 23 | `EVENT_CLASS_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Copy of the Event_Class_Source_Flag from the Contributor_system Table |
| 24 | `GROUPER_HOLD_TIME` | DOUBLE |  |  | Copy of the Grouper_Hold_Time from the Contributor_system Table |
| 25 | `GROUPER_MULTI_ORDS_IND` | DOUBLE |  |  | Copy of the Grouper_Multi_Ords_Ind from the Contributor_system Table |
| 26 | `IO_RESULT_IND` | DOUBLE | NOT NULL |  | Indicates whether the IO results from interface will be post to ce_intake_output_resut table. |
| 27 | `LISTENER_ALIAS` | VARCHAR(48) | NOT NULL |  | The selected listener alias is used for outbound document processing through devices associated to this Contributor System |
| 28 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Copy of the Loc_Facility_Cd from the Contributor_system Table |
| 29 | `MAX_GROUPER_ORDERS` | DOUBLE |  |  | Copy of the Max_Grouper_Orders from the Contributor_system Table |
| 30 | `MESSAGE_FORMAT_CD` | DOUBLE | NOT NULL |  | Copy of the Message_Format_Cd from the Contributor_system Table 25453 |
| 31 | `MICRO_LIST_REPLACE_FLAG` | DOUBLE | NOT NULL |  | Copy of the Micro_List_Replace_Flag from the Contributor_system Table |
| 32 | `MICRO_MULTI_INTERP_IND` | DOUBLE |  |  | Copy of the Micro_Multi_Interp_Ind from the Contributor_system Table |
| 33 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made new modification on the Contributor_System table |
| 34 | `OPF_MATCH_THRESHOLD` | CHAR(3) |  |  | Copy of the Opf_Match_Threshold from the Contributor_system Table |
| 35 | `OPF_REPORT_THRESHOLD` | CHAR(3) |  |  | Copy of the Opf_Report_Threshold from the Contributor_system Table |
| 36 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Copy of the Organization_id from the Contributor_system Table |
| 37 | `ORG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made original modification on the Contributor_System table |
| 38 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Copy of the Prsnl_Person_ID from the Contributor_system Table |
| 39 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Beg_Eff_Dt_TM from the Contributor_system Table |
| 40 | `RESULT_ALIAS_IND` | DOUBLE |  |  | Copy of the Result_Alias_Ind from the Contributor_system Table |
| 41 | `SI_CONTRIBUTOR_SYSTEM_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 42 | `SYS_DIRECTION_CD` | DOUBLE | NOT NULL |  | Copy of the Sys_Direction_Cd from the Contributor_system Table |
| 43 | `TIME_ZONE` | VARCHAR(100) |  |  | Copy of the Time_Zone from the Contributor_system Table |
| 44 | `TIME_ZONE_FLAG` | DOUBLE | NOT NULL |  | Copy of the Time_Zone_Flag from the Contributor_system Table |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

