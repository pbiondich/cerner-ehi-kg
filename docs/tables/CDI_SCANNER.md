# CDI_SCANNER

> This table defines the network scanners available in the system.

**Description:** cdi scanner  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_CORRECT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the scanner should automatically clean up the image. |
| 2 | `BRIGHTNESS` | DOUBLE |  |  | Default brightness level of the scanned image. |
| 3 | `BUILDING_CD` | DOUBLE | NOT NULL |  | Building in which the scanner is located. |
| 4 | `CDI_SCANNER_ID` | DOUBLE | NOT NULL |  | Unique identifier for each row (scanner) in the system. |
| 5 | `CONTRAST_CD` | DOUBLE | NOT NULL |  | Default contrast level of the scanned image. |
| 6 | `DEPTH_CD` | DOUBLE | NOT NULL |  | Default color depth used when scanning. |
| 7 | `DUPLEX_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to scan in duplex. |
| 8 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility in which the scanner is located. |
| 9 | `JPEG_QUALITY` | DOUBLE |  |  | Default quality for JPEG images. Valid values are 5 - 95. Higher number means higher quality, lower number means smaller file size. |
| 10 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Nurse unit in which the scanner is located. |
| 11 | `ORIENTATION` | DOUBLE | NOT NULL |  | Default page orientation of document being scanned. 0 = Portrait; 1 = Landscape. |
| 12 | `RESOLUTION_CD` | DOUBLE | NOT NULL |  | Default resolution to be used when scanning. |
| 13 | `ROOM_CD` | DOUBLE | NOT NULL |  | Room in which the scanner is located. |
| 14 | `SCANNER_DESCRIPTION` | VARCHAR(200) | NOT NULL |  | Text description of the scanner. |
| 15 | `SCANNER_IP_ADDRESS` | VARCHAR(15) | NOT NULL |  | ip address of scanner |
| 16 | `SCANNER_NAME` | VARCHAR(100) | NOT NULL |  | Name of the scanner. |
| 17 | `SCANNER_PATH` | VARCHAR(200) | NOT NULL |  | Network path to be used for temporary image storage during scanning. |
| 18 | `SIZE_CD` | DOUBLE | NOT NULL |  | Default page size of document being scanned. |
| 19 | `TIMEOUT` | DOUBLE | NOT NULL |  | Number of minutes the system will wait for the user to scan a document prior to timing out. |
| 20 | `TYPE_CD` | DOUBLE | NOT NULL |  | Default file type the images will be scanned in from this device. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

