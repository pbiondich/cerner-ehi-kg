# CS_CPP_TIER

> Tier information for the pre-qualification of charges for the new charge preprocessor framework prior to running rules.

**Description:** Charge Services - Charge Preprocessor Tier  
**Table type:** REFERENCE  
**Primary key:** `CS_CPP_TIER_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 3 | `CHARGE_STATUS_IND` | DOUBLE | NOT NULL |  | Indicates the rule will ignore the charge status of other charges on each encounter or not. 0 -No, 1-Yes |
| 4 | `CS_CPP_RULESET_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the ruleset related to this tier. |
| 5 | `CS_CPP_TIER_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a charge preprocessor tier. |
| 6 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type of the patient. This column is OBSOLETE. |
| 7 | `ENCNTR_TYPE_CLASS_EXCLD_IND` | DOUBLE | NOT NULL |  | Specifies whether to use the encntr_type_class_detail as a tier qualifier. |
| 8 | `ENCNTR_TYPE_EXCLD_IND` | DOUBLE | NOT NULL |  | Specifies whether to use the encntr_type_cd as a tier quailifier or to qualify all encounter types except the one specified. (0 = Don't Exclude, 1 = Do Exclude) |
| 9 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Contains the Financial Class of the patient. This column is OBSOLETE. |
| 10 | `FIN_CLASS_EXCLD_IND` | DOUBLE | NOT NULL |  | Specifies whether to use the fin_class_cd as a tier quailifier or to qualify all financial classes except the one specified. (0 = Don't Exclude, 1 = Do Exclude) |
| 11 | `HEALTH_PLAN_EXCLD_IND` | DOUBLE | NOT NULL |  | Specifies whether to use the health_plan_id as a tier quailifier or to qualify all health plans except the one specified. (0 = Don't Exclude, 1 = Do Exclude) |
| 12 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Health Plan related to this Tier. This column is OBSOLETE. |
| 13 | `INS_ORG_EXCLD_IND` | DOUBLE | NOT NULL |  | Specifies whether to use the ins_org_id as a tier quailifier or to qualify all insurance organizations except the one specified. (0 = Don't Exclude, 1 = Do Exclude) |
| 14 | `INS_ORG_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Insurance Organization related to this tier. This column is OBSOLETE. |
| 15 | `ORGANIZATION_EXCLD_IND` | DOUBLE | NOT NULL |  | Specifies whether to use the Organization_ID as a tier quailifier or to qualify all organizations except the one specified. (0 = Don't Exclude, 1 = Do Exclude) |
| 16 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Uniquely Identifies the organization related to this tier. This column is OBSOLETE. |
| 17 | `PRIORITY_NBR` | DOUBLE | NOT NULL |  | The execution priority. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CS_CPP_TIER_DETAIL](CS_CPP_TIER_DETAIL.md) | `CS_CPP_TIER_ID` |

