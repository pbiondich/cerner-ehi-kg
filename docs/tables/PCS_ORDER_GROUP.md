# PCS_ORDER_GROUP

> Stores a group identifier for linking patient orders.

**Description:** PathNet Common Services Order Group  
**Table type:** ACTIVITY  
**Primary key:** `PCS_ORDER_GROUP_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_CLASS_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the accession class related to this row. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `GROUP_ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the accession number associated with the group identifier. |
| 7 | `GROUP_NAME` | VARCHAR(40) | NOT NULL |  | Contains the group name display value. |
| 8 | `GROUP_NAME_KEY` | VARCHAR(40) | NOT NULL |  | Uniquely identifies the name of a given group used for linking patient orders. The format is in uppercase with spaces and special characters removed. |
| 9 | `GROUP_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | GROUP_NAME_KEY_A_NLS column |
| 10 | `GROUP_NAME_KEY_NLS` | VARCHAR(82) | NOT NULL |  | Stores the name of the group in corresponding non-English character set values. |
| 11 | `GROUP_STATUS_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the status of the group identifier. For example: open, closed, etc. |
| 12 | `PCS_ORDER_GROUP_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a group identifier for linking patient orders. |
| 13 | `PREV_PCS_ORDER_GROUP_ID` | DOUBLE | NOT NULL |  | Used to track version of the order group. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCS_ORDER_GROUP_R](PCS_ORDER_GROUP_R.md) | `PCS_ORDER_GROUP_ID` |

