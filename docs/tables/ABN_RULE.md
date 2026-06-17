# ABN_RULE

> Contains 'rules' around a particular icd-9/cpt-4 combination to determine if it's reimburseable.

**Description:** ABN RULE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_RULE_ID` | DOUBLE | NOT NULL |  | primary key for this table |
| 2 | `ACTION_CD` | DOUBLE | NOT NULL |  | Code value associated with a certain action. For example AD for added diagnosis code |
| 3 | `ACTION_CD_DT_TM` | DATETIME |  |  | date associated with the certain action code. |
| 4 | `ACTION_CODE` | VARCHAR(200) |  |  | Action Code |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 8 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 9 | `AGE_RESTRICTION_CODE` | VARCHAR(50) |  |  | Age restriction for the procedure. "<" means less than or equal to and ">" means greater than or equal to. For example, >50 means that a service is limited to someone 50 years of age or older. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `CARRIER_ID` | DOUBLE | NOT NULL |  | ID FOR THE INSURANCE CARRIER. Obsolete Column. Not used |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `CPT_NOMEN_ID` | DOUBLE | NOT NULL |  | Nomenclature id of the CPT-4 code. |
| 14 | `ENCNTR_GROUP_CD` | DOUBLE | NOT NULL |  | Encounter Group Code |
| 15 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type code that this rule qualifies for |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class code that this rule qualifies for |
| 18 | `FIN_GROUP_CD` | DOUBLE | NOT NULL |  | Financial Group Code |
| 19 | `FREQUENCY_REST_CODE` | VARCHAR(50) |  |  | Frequency restriction for a procedure. Standard format is one procedure per certain time period. For instance , no more than 2 x-rays per week/month/year etc. Written with number and time period, e.g. 11M means one procedure every eleven months. |
| 20 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Health plan id associated with the rule. |
| 21 | `ICD9_NOMEN_ID` | DOUBLE | NOT NULL |  | Nomenclature id for the diagnosis code |
| 22 | `INFOX_POLICY_NUMBER` | VARCHAR(100) |  |  | Info-X Policy Number |
| 23 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Long_text_id for the corresponding memo in the long text table. |
| 24 | `MEDICARE_POLICY_NUMBER` | VARCHAR(100) |  |  | Medicare Policy Number |
| 25 | `PARAMETER_CD` | DOUBLE | NOT NULL |  | Parameters or additional info related with abn_rule. For example, screening tests - no ICD-9 codes required, non-covered procedures, and non-covered diagnosis explicitly listed in policies. |
| 26 | `POLICY_DISCRIPTION` | VARCHAR(200) |  |  | A brief description of the policy. |
| 27 | `POLICY_NAME` | VARCHAR(100) |  |  | Policy name |
| 28 | `POLICY_NUMBER` | DOUBLE |  |  | Policy number |
| 29 | `SEX_RESTRICTION_CODE` | VARCHAR(10) |  |  | Sex restriction for the procedure. |
| 30 | `TYPE_CD` | DOUBLE | NOT NULL |  | Type or category. For example, anesthesiology, neurology, medications, and radiology etc. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `URL` | VARCHAR(100) |  |  | WorldWideWeb (WWW) link if available for a given policy. |
| 37 | `VALID_DIAG_FLG` | DOUBLE |  |  | Tells if this diagnosis is, is not, or none are reimbursable on this CPT-4. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

