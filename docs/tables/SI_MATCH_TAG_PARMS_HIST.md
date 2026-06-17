# SI_MATCH_TAG_PARMS_HIST

> This table stores historical information for the match_tag_parms table.

**Description:** System Integration Match Tag Parms History  
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
| 5 | `ALIAS_ENTITY_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Copy of the Alias_Entity_Alias_Type_cd field from the match_tag_parms table. |
| 6 | `ALIAS_ENTITY_NAME` | VARCHAR(32) |  |  | Copy of the Alias_entity_Name field from the match_tag_parms table. |
| 7 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Copy of the Alias_Pool_Cd field from the match_tag_parms table. |
| 8 | `BILLING_IND` | DOUBLE |  |  | Copy of the Billing_ind field from the match_tag_parms table. |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `MATCH_FIELD_CD` | DOUBLE | NOT NULL |  | Copy of the Match_Field_cd field from the match_tag_parms table. |
| 11 | `MATCH_FUNCTION_CD` | DOUBLE | NOT NULL |  | Copy of the Match_Function_cd field from the match_tag_parms table. |
| 12 | `MATCH_SEQ` | DOUBLE |  |  | Copy of the Match_Seq field from the match_tag_parms table. |
| 13 | `MATCH_TAG_PARMS_ID` | DOUBLE | NOT NULL |  | Copy of the Match_Tag_Parms_id field from the match_tag_parms table. |
| 14 | `MATCH_VALIDATION_CD` | DOUBLE | NOT NULL |  | Copy of the Match_validation_cd field from the match_tag_parms table. |
| 15 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made new modification on the match_tag_parms table |
| 16 | `OPF_IND` | DOUBLE |  |  | Copy of the Opf_ind field from the match_tag_parms table. |
| 17 | `ORDER_CONTROL_CD` | DOUBLE | NOT NULL |  | Copy of the Order_Control_cd field from the match_tag_parms table. |
| 18 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made original modification on the match_tag_parms table |
| 19 | `PRIM_ALIAS_IND` | DOUBLE |  |  | Copy of the Prim_Alias_Ind field from the match_tag_parms table. |
| 20 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Rec_Beg_Eff_Dt_TM field from the match_tag_parms table. |
| 21 | `SI_MATCH_TAG_PARMS_HIST_ID` | DOUBLE | NOT NULL |  | SI_match_tag_parms_Hist_id Primary Key |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `WEIGHT` | DOUBLE |  |  | Copy of the Weight field from the match_tag_parms table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

