# PHYS_COUNT_SHEET_ITEM

> Stores the items that will be counted on the physical count sheet.

**Description:** Physical Count Sheet Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABC_CLASS_CD` | DOUBLE | NOT NULL |  | The ABC classification for the item. |
| 2 | `AVERAGE_COST_AMT` | DOUBLE | NOT NULL |  | Average cost of the item while the physical count sheet is committed. |
| 3 | `BUILD_IND` | DOUBLE |  |  | Indicates whether or not the location records will need to be created. |
| 4 | `COMMIT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not an adjustment transaction has been performed. |
| 5 | `COUNT_QTY` | DOUBLE |  |  | The quantity that was counted. |
| 6 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 7 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 8 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 9 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 10 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to item_master table. |
| 11 | `LAST_COST_AMT` | DOUBLE | NOT NULL |  | Laswt cost of the item while the physical count sheet is committed. |
| 12 | `LAST_COUNT_DT_TM` | DATETIME |  |  | The last date that this item was counted for this sheet. |
| 13 | `LINE_NBR` | DOUBLE |  |  | The line number for this sheet. |
| 14 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location |
| 15 | `LOCATOR_CD` | DOUBLE | NOT NULL |  | The physical location where the item is kept. |
| 16 | `MULTIPLE_IND` | DOUBLE |  |  | Indicates that an item exists on more than one sheet for the same package type but different locators. |
| 17 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | A foreign key to the package type table. This is the package that is being counted. |
| 18 | `PERPETUAL_IND` | DOUBLE | NOT NULL |  | Indicates if this item is defined as Perpetual or Non-Perpetual for this count. |
| 19 | `PHYS_COUNT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key |
| 20 | `QOH_QTY` | DOUBLE |  |  | The quantity-on-hand that was present when the count was started. |
| 21 | `SHEET_NBR` | DOUBLE | NOT NULL | FK→ | Value that depicts the sheet the item is assigned on. |
| 22 | `SORT_VALUE1` | VARCHAR(200) |  |  | Sort Value |
| 23 | `SORT_VALUE2` | VARCHAR(200) |  |  | Sort Value |
| 24 | `SORT_VALUE3` | VARCHAR(200) |  |  | Sort Value |
| 25 | `SORT_VALUE4` | VARCHAR(200) |  |  | Sort Value |
| 26 | `SORT_VALUE5` | VARCHAR(200) |  |  | Sort Value |
| 27 | `SORT_VALUE_KEY1` | VARCHAR(200) |  |  | Sort Value Key |
| 28 | `SORT_VALUE_KEY2` | VARCHAR(200) |  |  | Sort Value Key |
| 29 | `SORT_VALUE_KEY3` | VARCHAR(200) |  |  | Sort Value Key |
| 30 | `SORT_VALUE_KEY4` | VARCHAR(200) |  |  | Sort Value Key |
| 31 | `SORT_VALUE_KEY5` | VARCHAR(200) |  |  | Sort Value Key |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PHYS_COUNT_ID` | [PHYS_COUNT_SHEET](PHYS_COUNT_SHEET.md) | `PHYS_COUNT_ID` |
| `SHEET_NBR` | [PHYS_COUNT_SHEET](PHYS_COUNT_SHEET.md) | `SHEET_NBR` |

