# PE_STATUS_REASON

> ProFit Encounter Status Reason

**Description:** PE STATUS REASON  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_HOLD_RPTS_SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicates whether or not encounter should be included on bill hold reports. 0 - Include encounter on bill hold reports, 1 - Don't include encounter on bill hold reports |
| 7 | `BO_HP_RELTN_ID` | DOUBLE |  | FK→ | Uniquely identifies the bo_hp_reltn to which this hold applies. |
| 8 | `CLAIM_SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicates whether or not claims should be held for the encounter. 0 - Generate claims, 1 - Hold claims |
| 9 | `COLL_SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicates whether the hold that it associated with the encounter is to be suppressed from sending to Collections. |
| 10 | `CORSP_SUPPRESS_IND` | DOUBLE |  |  | Indicates whether or not correspondence should be held for the encounter. 0 - generate correspondence1 - hold correspondence |
| 11 | `DUNNING_SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicates whether the hold that it associated with the encounter should have dunning messages suppressed from the statement. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `GUAR_ACCT_ID` | DOUBLE |  | FK→ | Uniquely identifies the account id of the guarantor for this record. |
| 14 | `INSURANCE_BO_ID` | DOUBLE |  |  | **Obsolete** - no longer used - Uniquely identifies the related benefit order on the benefit_order table. **Obsolete** |
| 15 | `PE_HOLD_DT_TM` | DATETIME |  |  | The date ProFit encounter was put on hold. |
| 16 | `PE_RELEASE_DT_TM` | DATETIME |  |  | The date and time on which the hold on the ProFit encounter was released. |
| 17 | `PE_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Describes the reason this hold was applied, e.g. standard delay period, waiting for encounter discharge. |
| 18 | `PE_STATUS_REASON_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a ProFit Encounter status reason. |
| 19 | `PE_SUB_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Provides additional information about the reason for applying this hole. This field is optional. |
| 20 | `PFT_BALANCE_ID` | DOUBLE |  | FK→ | Identifies the associated account with a balance level hold |
| 21 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the pft_encntr to which this hold has been applied. |
| 22 | `PFT_HOLD_ID` | DOUBLE | NOT NULL | FK→ | FK to the pft_hold table |
| 23 | `PRECOLL_SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicates whether the hold that it associated with the encounter is to be suppressed from sending to PreCollections. |
| 24 | `REASON_COMMENT` | VARCHAR(40) |  |  | User-defined text comment that gives reason for placing a hold |
| 25 | `STMT_SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicates whether or not statements should be held for the encounter. 0 - Generate statements, 1 - Hold statements |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `GUAR_ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `PFT_BALANCE_ID` | [PFT_BALANCE](PFT_BALANCE.md) | `PFT_BALANCE_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `PFT_HOLD_ID` | [PFT_HOLD](PFT_HOLD.md) | `PFT_HOLD_ID` |

