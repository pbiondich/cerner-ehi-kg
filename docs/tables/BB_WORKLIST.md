# BB_WORKLIST

> Stores the high-level Blood Bank worklist information. Worklists are created as a means of quickly saving and loading groups of Blood Bank orders.

**Description:** Blood Bank Worklist  
**Table type:** ACTIVITY  
**Primary key:** `WORKLIST_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time the worklist was created. |
| 2 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code of the personnel that created the worklist. |
| 3 | `DOWNLOAD_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the worklist has been downloaded to the instrument queue. |
| 4 | `LAST_DOWNLOAD_DT_TM` | DATETIME |  |  | Contains the date and time the worklist was last downloaded. |
| 5 | `QC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code of the Quality Control Group associated with the worklist. |
| 6 | `TEST_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code of the Test Group associated with the worklist. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WORKLIST_ID` | DOUBLE | NOT NULL | PK | Contains the internal identification code that uniquely identifies the worklist. |
| 13 | `WORKLIST_NAME` | VARCHAR(40) | NOT NULL |  | Contains the display name for the worklist. |
| 14 | `WORKLIST_NAME_KEY` | VARCHAR(40) | NOT NULL |  | Contains the display key of the worklist. |
| 15 | `WORKLIST_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | WORKLIST_NAME_KEY_A_NLS column |
| 16 | `WORKLIST_NAME_KEY_NLS` | VARCHAR(82) | NOT NULL |  | This field contains the same data as the worklist_name_key only stored in the corresponding non-English character set values for _key. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `QC_GROUP_ID` | [BB_QC_GROUP](BB_QC_GROUP.md) | `GROUP_ID` |
| `TEST_GROUP_ID` | [BB_TEST_GROUP](BB_TEST_GROUP.md) | `BB_TEST_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_WORKLIST_DETAIL](BB_WORKLIST_DETAIL.md) | `WORKLIST_ID` |

