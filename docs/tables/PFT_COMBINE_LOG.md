# PFT_COMBINE_LOG

> Store the inforamtion related to various ProFit combine processes.

**Description:** PFT COMBINE LOG  
**Table type:** ACTIVITY  
**Primary key:** `PFT_COMBINE_LOG_ID`  
**Columns:** 27  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_PERSON_RELTN_ID` | DOUBLE | NOT NULL |  | References to a relation record in the in acct_person_reltn table. This corresponds to the FROM person of the FROM/TO combine pair. This field is left NULL if the FROM person's role type anything other than Guarantor - No longer used |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CHARGE_ITEM_ID` | DOUBLE |  | FK→ | Unique identifier of the charge that was reassociated from charge group to another. It is null for all combine types except Modify Charge Group. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FROM_ENCNTR_ID` | DOUBLE |  | FK→ | Contains the Encounter Identifier belonging to the from side of the combine. |
| 10 | `FROM_XXX_ID` | DOUBLE | NOT NULL |  | Reference to the person or encounter table.Identiifes the FROM item in the FROM/TO pair of Person/Encounter combine. |
| 11 | `PFT_COMBINE_LOG_ID` | DOUBLE | NOT NULL | PK | System generated number used to uniquely identify a row on the PFT_COMBINE_LOG table. |
| 12 | `PFT_COMBINE_TYPE_CD` | DOUBLE | NOT NULL |  | Code value indicating the type of combine (e.g. Person, Encounter etc.) |
| 13 | `RESOLVED_DT_TM` | DATETIME |  |  | The date and time when the combine situation was resolved in ProFit. This gives the date and time when the manual combine (Person or Encounter) within ProFit was completed. |
| 14 | `RESOLVED_IND` | DOUBLE |  |  | Indicator telling whether the combine process within ProFit has been completed. A value of 0 or 1 indicate and incomplete or complete combine respectively. |
| 15 | `RESOLVED_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the person who manually completed the combine within ProFit. |
| 16 | `RULE_DESC` | VARCHAR(350) |  |  | The description of the rule/reason that caused the combine/linking. |
| 17 | `RULE_IDENT` | VARCHAR(200) |  |  | The identifier that defines uniqueness of a rule/reason that caused the combine/linking. |
| 18 | `RULE_VERSION` | VARCHAR(200) |  |  | Contains a version number for the rule. |
| 19 | `SOURCE_FLAG` | DOUBLE | NOT NULL |  | Identifies classification of the source feed from which a set of data originated from. |
| 20 | `TO_ENCNTR_ID` | DOUBLE |  | FK→ | Uniquely identifies the related encounter identifier on the to side of the combine. |
| 21 | `TO_XXX_ID` | DOUBLE | NOT NULL |  | Reference to the person or encounter table. Identiifes the TO item in the FROM/TO pair of Person/Encounter combine. |
| 22 | `UNCOMBINE_IND` | DOUBLE |  |  | Indicates that the combine pair needs to be uncombined. 1 indicated that uncombine is needed. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |
| `FROM_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `TO_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_COMBINE_RULE](PFT_COMBINE_RULE.md) | `PFT_COMBINE_LOG_ID` |

