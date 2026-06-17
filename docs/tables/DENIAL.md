# DENIAL

> This table tracks denial information on the claims.

**Description:** Denial  
**Table type:** ACTIVITY  
**Primary key:** `DENIAL_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_TRANS_FILE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the batch transaction associated with a denial. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILL_VRSN_NBR` | DOUBLE |  | FK→ | The version number identifying which bill |
| 8 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Correspondence Activity ID value related to this denial. |
| 9 | `DENIAL_AMT` | DOUBLE | NOT NULL |  | Contains the amount of the denial. |
| 10 | `DENIAL_CODE_TXT` | VARCHAR(255) |  |  | The actual denial code sent on an ERA |
| 11 | `DENIAL_GROUP_CD` | DOUBLE | NOT NULL |  | Grouping mechanism for the Denial codes. |
| 12 | `DENIAL_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies denial information. |
| 13 | `DENIAL_REASON_CD` | DOUBLE | NOT NULL |  | Represents the denial reason on an era, if it is available. |
| 14 | `DENIAL_TXT` | VARCHAR(255) |  |  | Contains a textual description of the denial. |
| 15 | `DENIAL_TYPE_CD` | DOUBLE | NOT NULL |  | This defines the base type of the denial code i.e. provider, patient, technical, information only. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `FIN_TRANS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the FIN_TRANS_GROUP table. |
| 18 | `JOURNAL_BO_RELTN_ID` | DOUBLE | NOT NULL |  | Journal Benefit Order Relation ID related to this denial. The parent table JOURNAL_BO_RELATION is obsolete. |
| 19 | `PFT_LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Claim line item related to the denial. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_TRANS_FILE_ID` | [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `BATCH_TRANS_FILE_ID` |
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |
| `FIN_TRANS_GROUP_ID` | [FIN_TRANS_GROUP](FIN_TRANS_GROUP.md) | `FIN_TRANS_GROUP_ID` |
| `PFT_LINE_ITEM_ID` | [PFT_LINE_ITEM](PFT_LINE_ITEM.md) | `PFT_LINE_ITEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DENIAL_DETAIL](DENIAL_DETAIL.md) | `DENIAL_ID` |

