# SI_ESI_ALIAS_TRANS_HIST

> This table stores historical information for the ESI_Alias_Trans table.

**Description:** System Integration ESI Alias Trans History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_ENSURE_PARMS_FLAG` | DOUBLE | NOT NULL |  | Copy of the Alias_Ensure_Parms_Flag field from the esi_alias_trans table. |
| 6 | `ALIAS_ENTITY_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Alias_Entity_Alias_Type_Cd field from the esi_alias_trans table. Code can flex - depends on alias entity name. |
| 7 | `ALIAS_ENTITY_NAME` | VARCHAR(32) |  |  | Copy of the Alias_Entity_Name field from the esi_alias_trans table. |
| 8 | `ALIAS_FILTER_CD` | DOUBLE | NOT NULL |  | Copy of the Alias_Filter_Cd field from the esi_alias_trans table. |
| 9 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Copy of the Alias_Pool_Cd field from the esi_alias_trans table. |
| 10 | `ASSIGN_AUTHORITY_SYS_CD` | DOUBLE | NOT NULL |  | Copy of the Assign_Authority_Sys_Cd field from the esi_alias_trans table. |
| 11 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 12 | `ELIGIBLE_FOR_QUERY_IND` | DOUBLE | NOT NULL |  | Indicates that this alias is eligible to be sent out for MPI queries. |
| 13 | `ESI_ALIAS_FIELD_CD` | DOUBLE | NOT NULL |  | Copy of the Esi_Alias_Field_Cd field from the esi_alias_trans table. |
| 14 | `ESI_ALIAS_TRANS_ID` | DOUBLE | NOT NULL |  | Copy of the Esi_Alias_Trans_ID field from the esi_alias_trans table. |
| 15 | `ESI_ALIAS_TYPE` | VARCHAR(50) |  |  | Copy of the Esi_Alias_Type field from the esi_alias_trans table. |
| 16 | `ESI_ASSIGN_AUTH` | VARCHAR(50) |  |  | Copy of the Esi_Assign_Auth field from the esi_alias_trans table. |
| 17 | `ESI_ASSIGN_FAC` | VARCHAR(50) |  |  | Copy of the Esi_Assign_Fac field from the esi_alias_trans table. |
| 18 | `ESI_SOURCE` | VARCHAR(50) | NOT NULL |  | Copy of the ESI_Source field from the esi_alias_trans table. |
| 19 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made new modification on the Contributor_System table |
| 20 | `ORG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made original modification on the Contributor_System table |
| 21 | `PERSON_PROC_OPT_CD` | DOUBLE | NOT NULL |  | Options for processing person information via ESI. |
| 22 | `PRSNL_FT_STRING` | VARCHAR(50) |  |  | Copy of the Prsnl_ft_string field from the esi_alias_trans table. |
| 23 | `PRSNL_PROC_OPT_CD` | DOUBLE | NOT NULL |  | Copy of the Prsnl_proc_opt_cd field from the esi_alias_trans table. |
| 24 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Beg_Eff_Dt_TM field from the esi_alias_trans table. |
| 25 | `SI_ESI_ALIAS_TRANS_HIST_ID` | DOUBLE | NOT NULL |  | SI_ESI_Alias_Trans_Hist_id Primary ID |
| 26 | `SKIP_STRING` | VARCHAR(100) |  |  | Copy of the Skip_String field from the esi_alias_trans table. |
| 27 | `TRUNC_SIZE` | DOUBLE |  |  | Copy of the Trunc_Size field from the esi_alias_trans table. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

